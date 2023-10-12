from pybtex.database.input import bibtex


def get_personal_data():
    name = ["Bálint", "Mucsányi"]
    email = "b.h.mucsanyi@gmail.com"
    twitter = "BalintMucsanyi"
    github = "bmucsanyi"
    linkedin = "bmucsanyi"
    bio_text = f"""
                <p>I am a Machine Learning MSc student at the <a href="https://uni-tuebingen.de/" target="_blank">University of Tübingen</a>, working in the <a href="https://scalabletrustworthyai.github.io/" target="_blank">STAI</a> group of Seong Joon Oh.</p>
                <p>
                    <span style="font-weight: bold;">Interests:</span> 
                    I am interested in probabilistic model architectures capable of representing different sources of uncertainty. My goal is to contribute to the theoretical foundations of uncertainty in machine learning while developing scalable practical solutions.
                    I am also excited about computer vision.
                </p>

                <p>
                    <span style="font-weight: bold;">Bio:</span> 
                    I received my BSc degree in Computer Science from ELTE Eötvös Loránd University in 2021 (Grade: Outstanding) with the Best Thesis and Outstanding Student of the Faculty awards. I previously worked on neural program synthesis with a focus on provable correctness.
                    I am currently writing my master's thesis about uncertainty quantification under the supervision of Seong Joon Oh and Michael Kirchhof.
                </p>
                <p>For any inquiries, feel free to reach out to me via mail!</p>
                <p>
                    <a href="https://bmucsanyi.github.io/assets/pdf/CV_Mucsanyi_Balint.pdf" target="_blank" style="margin-right: 15px"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:{email}" style="margin-right: 15px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/{twitter}" target="_blank" style="margin-right: 15px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                    <a href="https://scholar.google.com/citations?user=NexA8EEAAAAJ&hl=en" target="_blank" style="margin-right: 15px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/{github}" target="_blank" style="margin-right: 15px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/{linkedin}" target="_blank" style="margin-right: 15px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Homepage Template</h4>
                <p>
                    This website is based on the template of <a href="https://m-niemeyer.github.io/" target="_blank">Michael Niemeyer</a>. Check out his <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">Github repository</a> for instructions on how to use it.
                </p>
            </div>
    """
    return name, bio_text, footer


def get_author_dict():
    return {
        "Seong Joon Oh": "https://coallaoh.github.io/",
        "Michael Kirchhof": "https://www.linkedin.com/in/michael-kirchhof/",
        "Enkelejda Kasneci": "https://www.edu.sot.tum.de/hctl/prof-dr-enkelejda-kasneci/",
        "Balázs Pintér": "https://scholar.google.com/citations?user=f2P5j8YAAAAJ&hl=en/",
        "Ádám Czapp": "https://scholar.google.com/citations?user=vSbbMVEAAAAJ&hl=en",
        "Bálint Gyarmathy": "https://scholar.google.com/citations?user=Ofo9RRcAAAAJ&hl=en",
        "Daniel Dauner": "https://danieldauner.github.io/",
    }


def generate_person_html(
    persons,
    connection=", ",
    make_bold=True,
    make_bold_name="Bálint Mucsányi",
    add_links=True,
):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in (
            p.get_part("first") + p.get_part("middle") + p.get_part("last")
        ):
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = (
                f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
            )
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s


def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if "award" in entry.fields.keys():
        s += f"""<a href="{entry.fields['pdf']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['pdf']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {
        "html": "Project Page",
        "pdf": "Paper",
        "supp": "Supplemental",
        "video": "Video",
        "poster": "Poster",
        "code": "Code",
    }
    i = 0
    for k, v in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += " / "
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f"[{entry_key}] Warning: Field {k} missing!")

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += (
        "\tauthor = {"
        + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}"
        + "}, \n"
    )
    for entr in ["title", "booktitle", "year"]:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += (
        " /"
        + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    )
    s += """ </div> </div> </div>"""
    return s


def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file("publication_list.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_paper_entry(k, bib_data.entries[k])
    return s


def get_misc_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file("miscellaneous_list.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_paper_entry(k, bib_data.entries[k])
    return s


def get_index_html():
    pub = get_publications_html()
    misc = get_misc_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container">
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="margin-bottom: 1em;">
            <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
            </div>
            <br>
            <div class="col-md-8" style="">
                {bio_text}
            </div>
            <div class="col-md-4" style="">
                <img src="assets/img/profile.jpg" class="img-thumbnail" width="280px" alt="Profile picture">
            </div>
        </div>
        <div class="row" style="margin-top: 1em;">
            <div class="col-sm-12" style="">
                <h4>Publications</h4>
                {pub}
            </div>
        </div>
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="">
                <h4>Miscellaneous</h4>
                {misc}
            </div>
        </div>
        <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
            {footer}
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename="index.html"):
    s = get_index_html()
    with open(filename, "w") as f:
        f.write(s)
    print(f"Written index content to {filename}.")


if __name__ == "__main__":
    write_index_html("index.html")
