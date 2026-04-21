from flask import Flask, render_template
from random import choice

app = Flask(__name__)

@app.route("/")
def main_site():
    return render_template("1 index.html")

@app.route("/tips")
def tips():
    return render_template("2 tips.html")

@app.route("/lineups")
def lineups():
    return render_template("2 lineups.html")

@app.route("/smokes")
def smokes():
    return render_template("b smokes.html")

@app.route("/mirage smokes")
def mirage_smokes():
    return render_template("c mirage smokes.html")

@app.route("/mirage smokes ct")
def mirage_smokes_ct():
    return render_template("d mirage smokes ct.html")

@app.route("/mirage smokes ct ramp")
def mirage_smokes_ct_ramp():
    return render_template("e mirage smokes ct ramp.html")

@app.route("/mirage smokes ct palace")
def mirage_smokes_ct_palace():
    return render_template("e mirage smokes ct palace.html")

@app.route("/mirage smokes ct right boxes")
def mirage_smokes_ct_right_boxes():
    return render_template("e mirage smokes ct right boxes.html")

@app.route("/mirage smokes ct entry")
def mirage_smokes_ct_entry():
    return render_template("e mirage smokes ct entry.html")

@app.route("/mirage smokes ct mid short")
def mirage_smokes_ct_mid_short():
    return render_template("e mirage smokes ct mid short.html")

@app.route("/mirage smokes ct under")
def mirage_smokes_ct_under():
    return render_template("e mirage smokes ct under.html")

@app.route("/mirage smokes ct b short")
def mirage_smokes_ct_b_short():
    return render_template("e mirage smokes ct b short.html")

@app.route("/mirage smokes ct appartments")
def mirage_smokes_ct_appartments():
    return render_template("e mirage smokes ct appartments.html")

@app.route("/mirage smokes ct bench")
def mirage_smokes_ct_bench():
    return render_template("e mirage smokes ct bench.html")

@app.route("/mirage smokes tt")
def mirage_smokes_tt():
    return render_template("d mirage smokes tt.html")

@app.route("/mirage smokes tt ct")
def mirage_smokes_tt_ct():
    return render_template("e mirage smokes tt ct.html")

@app.route("/mirage smokes tt jungle")
def mirage_smokes_tt_jungle():
    return render_template("e mirage smokes tt jungle.html")

@app.route("/mirage smokes tt stairs")
def mirage_smokes_tt_stairs():
    return render_template("e mirage smokes tt stairs.html")

@app.route("/mirage smokes tt window")
def mirage_smokes_tt_window():
    return render_template("e mirage smokes tt window.html")

@app.route("/mirage smokes tt connector")
def mirage_smokes_tt_connector():
    return render_template("e mirage smokes tt connector.html")

@app.route("/molotovs")
def molotovs():
    return render_template("b molotovs.html")

@app.route("/mirage molotovs")
def mirage_molotovs():
    return render_template("c mirage molotovs.html")

@app.route("/flashes")
def flashes():
    return render_template("b flashes.html")

@app.route("/mirage flashes")
def mirage_flashes():
    return render_template("c mirage flashes.html")

app.run(debug=True)