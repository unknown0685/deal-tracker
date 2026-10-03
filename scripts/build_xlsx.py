"""Build Tracker.xlsx from the append-only CSVs in data/.

Run from repo root:  python scripts/build_xlsx.py
Every summary number on the Dashboard is a live formula over the data sheets;
charts are native Excel charts. Each data row keeps its source URL.
"""
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
HDR_FILL = PatternFill("solid", fgColor="1F3864")
HDR_FONT = Font(bold=True, color="FFFFFF")
NUMERIC = {"value_usd_bn", "spx", "spx_pct", "ndx_comp", "ndx_comp_pct", "dow", "dow_pct",
           "rut", "rut_pct", "ust2y", "ust10y", "ust30y", "fed_funds_upper", "brent", "wti", "gold", "vix"}


def read(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    return rows[0], rows[1:]


def conv(col, v):
    if col in NUMERIC and v.strip():
        try:
            return float(v.replace(",", ""))
        except ValueError:
            return v
    return v


def sheet_from_csv(wb, title, fname, widths=None, table_name=None):
    header, rows = read(fname)
    ws = wb.create_sheet(title)
    ws.append(header)
    for r in rows:
        r = (r + [""] * len(header))[: len(header)]
        ws.append([conv(c, v) for c, v in zip(header, r)])
    for i, h in enumerate(header, 1):
        c = ws.cell(1, i)
        c.fill, c.font = HDR_FILL, HDR_FONT
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(h, max(10, min(40, len(h) + 4)))
        if h == "source":
            for row in range(2, ws.max_row + 1):
                cell = ws.cell(row, i)
                if str(cell.value).startswith("http"):
                    cell.hyperlink = cell.value
                    cell.font = Font(color="0563C1", underline="single")
    ws.freeze_panes = "B2"
    if rows and table_name:
        ref = f"A1:{get_column_letter(len(header))}{len(rows) + 1}"
        t = Table(displayName=table_name, ref=ref)
        t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
        ws.add_table(t)
    return ws, header, len(rows)


def col(header, name):
    return get_column_letter(header.index(name) + 1)


def main():
    wb = Workbook()
    dash = wb.active
    dash.title = "Dashboard"

    deals, dh, nd = sheet_from_csv(wb, "Deals", "deals.csv",
                                   {"deal": 34, "rationale": 50, "source": 50, "target": 26,
                                    "acquirer_or_investor": 30}, "DealsTbl")
    mk, mh, nm = sheet_from_csv(wb, "Markets", "markets.csv", {"notes": 50, "source": 50}, "MarketsTbl")
    me, eh, ne = sheet_from_csv(wb, "MacroEvents", "macro_events.csv", {"event": 60, "source": 50}, "MacroTbl")
    fh, frows = read("../firms.csv")
    fs = wb.create_sheet("Firms")
    fs.append(fh + ["deals_logged", "page"])
    for r in frows:
        fs.append(r)
    cf = col(dh, "covered_firms")
    for i in range(2, len(frows) + 2):
        fs.cell(i, 5).value = f'=COUNTIF(Deals!${cf}:${cf},"*"&A{i}&"*")'
        fs.cell(i, 6).value = f"firms/{fs.cell(i, 1).value}.md"
    for i in range(1, 7):
        fs.cell(1, i).fill, fs.cell(1, i).font = HDR_FILL, HDR_FONT
    for c, w in zip("ABCDEF", (20, 30, 34, 16, 14, 30)):
        fs.column_dimensions[c].width = w

    # Dashboard: live formulas over the data sheets
    dash["A1"] = "Interview-Ready Tracker"
    dash["A1"].font = Font(bold=True, size=16)
    dash["A2"] = "All figures below are formulas over the Deals / Markets sheets; each data row carries its source URL."
    dash["A2"].alignment = Alignment(wrap_text=False)

    def last(colname):  # last non-blank value in a Markets column
        c = col(mh, colname)
        return f'=IFERROR(LOOKUP(2,1/(Markets!{c}2:{c}10000<>""),Markets!{c}2:{c}10000),"n/a")'

    rows = [("Latest market prints", None),
            ("Latest date with data", last("date")),
            ("S&P 500", last("spx")), ("Nasdaq Composite", last("ndx_comp")),
            ("Dow", last("dow")), ("Russell 2000", last("rut")),
            ("2y UST %", last("ust2y")), ("10y UST %", last("ust10y")), ("30y UST %", last("ust30y")),
            ("Fed funds upper %", last("fed_funds_upper")), ("WTI $", last("wti")), ("Brent $", last("brent")),
            ("", None), ("Deal ledger", None)]
    vc, st, dt = col(dh, "value_usd_bn"), col(dh, "status"), col(dh, "deal_type")
    rows += [("Deals logged", f"=COUNTA(Deals!A2:A100000)"),
             ("Disclosed value logged ($bn)", f"=SUM(Deals!{vc}:{vc})"),
             ("…of which ANNOUNCED", f'=COUNTIF(Deals!{st}:{st},"ANNOUNCED")'),
             ("…of which REPORTED / RUMOR", f'=COUNTIF(Deals!{st}:{st},"REPORTED")+COUNTIF(Deals!{st}:{st},"RUMOR")')]
    r0 = 4
    for i, (label, f) in enumerate(rows):
        dash.cell(r0 + i, 1, label)
        if f is None and label:
            dash.cell(r0 + i, 1).font = Font(bold=True)
        elif f:
            dash.cell(r0 + i, 2, f)
    dash.column_dimensions["A"].width = 34
    dash.column_dimensions["B"].width = 16

    # deals-by-type block (formula-driven) for the bar chart
    types = ["M&A", "LBO", "Take-private", "RE", "Infra", "Private credit", "Fundraise",
             "Exit/IPO", "Secondaries", "Restructuring", "Minority/Growth"]
    dash["D3"], dash["E3"], dash["F3"] = "Deal type", "Count", "$bn disclosed"
    for c in ("D3", "E3", "F3"):
        dash[c].font = Font(bold=True)
    for i, t in enumerate(types, start=4):
        dash.cell(i, 4, t)
        dash.cell(i, 5, f'=COUNTIF(Deals!{dt}:{dt},D{i})')
        dash.cell(i, 6, f'=SUMIF(Deals!{dt}:{dt},D{i},Deals!{vc}:{vc})')
    dash.column_dimensions["D"].width = 16
    bar = BarChart()
    bar.title, bar.y_axis.title = "Deals logged by type", "Count"
    bar.add_data(Reference(dash, min_col=5, min_row=3, max_row=3 + len(types)), titles_from_data=True)
    bar.set_categories(Reference(dash, min_col=4, min_row=4, max_row=3 + len(types)))
    bar.height, bar.width = 7, 14
    dash.add_chart(bar, "H3")

    # Market line charts on the Markets sheet
    if nm:
        dcol = mh.index("date") + 1
        cats = Reference(mk, min_col=dcol, min_row=2, max_row=nm + 1)
        for idx, (series, title, anchor) in enumerate(
                [(("ust2y", "ust10y", "ust30y"), "Treasury yields (%)", "A"),
                 (("spx",), "S&P 500", "K")]):
            ch = LineChart()
            ch.title = title
            for s in series:
                c = mh.index(s) + 1
                ch.add_data(Reference(mk, min_col=c, min_row=1, max_row=nm + 1), titles_from_data=True)
            ch.set_categories(cats)
            ch.height, ch.width = 7, 14
            dash.add_chart(ch, f"{'H' if idx == 0 else 'H'}{18 + idx * 15}")

    out = ROOT / "Tracker.xlsx"
    wb.save(out)
    print(f"Wrote {out} — {nd} deals, {nm} market rows, {ne} macro events")


if __name__ == "__main__":
    main()
