from flask import Flask, render_template

from Grab_Google_Sheet import get_df


app = Flask(__name__)

@app.route("/")
def hello_world():
    projects = []
    df = get_df()
    available_projects = df.loc[df["State"]=="Yes"]
    for index, row in available_projects.iterrows():
        header = row["title"]
        description = row["description"]
        image = f"images/{row['image']}"
        url = row['url']
        projects.append({"Header": header, "Description": description, "Image": image, "Url": url})

        index = len(projects)/2
    return render_template('homepage.html', data=projects, index=int(index))