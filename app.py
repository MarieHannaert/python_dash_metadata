import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import os
import json
from datetime import date

# Initialiseer de Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definieer de layout
# Definieer de layout
app.layout = dbc.Container([
    html.H1("Metadata Form"),
    dcc.Markdown('''
    It is very import to **fill in the metadata** of your data.  
    If this is not filled in correctly your data will not be saved on our LTS *(long term storage)*. 
    '''),

    dbc.Form([
        dbc.Row([
            dbc.Label("Location", className="fw-bold"),
            dbc.Input(id="location", type="text", placeholder="Enter location"),
        ]),
        dbc.Row([
            dbc.Label("Project Name", className="fw-bold"),
            dbc.Input(id="project_name", type="text", placeholder="Fill in the Project Name"),
        ]),
        dbc.Row([
            dbc.Label("Project Description", className="fw-bold"),
            dbc.Textarea(id="project_description", placeholder="Give a small project description"),
        ]),
        dbc.Row([
            dbc.Label("Start Project Date", className="fw-bold"),
            dcc.DatePickerSingle(
                id="project_start_date",
                min_date_allowed=date(1995, 1, 1),
                max_date_allowed=date(2030, 2, 28),
                initial_visible_month=date.today(),
                date=date.today()
            ),
        ]),
        dbc.Row([
            dbc.Label("End Project Date", className="fw-bold"),
            dcc.DatePickerSingle(
                id="project_end_date",
                min_date_allowed=date(1995, 1, 1),
                max_date_allowed=date(2030, 2, 28),
                initial_visible_month=date.today(),
                date=date.today()
            ),
        ]),
        dbc.Row([
            dbc.Label("Project Size", className="fw-bold"),
            dbc.Input(id="project_size", type="text", placeholder="Estimation of size of the project"),
        ]),
        dbc.Row([
            dbc.Label("Project Status", className="fw-bold"),
            dbc.Input(id="project_status", type="text", placeholder="e.g., submitted, in progress, completed"),
        ]),
        dbc.Row([
            dbc.Label("User Name", className="fw-bold"),
            dbc.Input(id="user_name", type="text", placeholder="Name of user requesting service"),
        ]),
        dbc.Row([
            dbc.Label("User Email", className="fw-bold"),
            dbc.Input(id="user_email", type="email", placeholder="Email address"),
        ]),
        dbc.Row([
            dbc.Label("Principal Investigator", className="fw-bold"),
            dcc.Dropdown(
                id="principal_investigator",
                options=[{"label": name, "value": name} for name in 
                         ["Bart Loeys", "Aline Verstraeten", "Maaike Alaerts", 
                          "Guy Van Camp", "Wim Van Hul", "Frank Kooy", 
                          "Marije Meuwissen", "Ken Op de Beeck"]],
                multi=True,
                placeholder="Select Principal Investigator(s)"
            ),
        ]),
        dbc.Row([
            dbc.Label("Collaborator", className="fw-bold"),
            dbc.Input(id="collaborator", type="text", placeholder="All the people that are involved in the project, and thus need access to the data"),
        ]),
        dbc.Row([
            dbc.Label("Service Type", className="fw-bold"),
            dbc.Input(id="service_type", type="text", placeholder="e.g., sequencing, analysis, consultation"),
        ]),
        dbc.Row([
            dbc.Label("Sample Type", className="fw-bold"),
            dbc.Input(id="sample_type", type="text", placeholder="e.g., DNA, RNA"),
        ]),
        dbc.Row([
            dbc.Label("Organism", className="fw-bold"),
            dbc.Input(id="organism", type="text", placeholder="Organism name"),
        ]),
        dbc.Row([
            dbc.Label("Reference Genome", className="fw-bold"),
            dbc.Input(id="reference_genome", type="text", placeholder="e.g., hg38, mm10"),
        ]),

        dcc.Markdown('''
        \n
        **Did you fill in everything?**\n
        Click the button below to submit your request.
        '''),

        html.Div(id="output_message", style={'color': 'red'}),

        dbc.Row([
            dbc.Button("Submit", id="submit", color="primary", className="fw-bold"),
        ])
    ])
])


@app.callback(
    Output("output_message", "children"),
    Input("submit", "n_clicks"),
    [State("location", "value"), State("project_name", "value"), State("project_description", "value"),
     State("project_start_date", "date"), State("project_end_date", "date"), State("project_size", "value"), State("project_status", "value"), State("user_name", "value"),
     State("user_email", "value"), State("principal_investigator", "value"), State("collaborator", "value"),
     State("service_type", "value"), State("sample_type", "value"), State("organism", "value"),
     State("reference_genome", "value")]
)
def save_metadata(n_clicks, location, project_name, project_description, project_start_date, project_end_date, project_size, project_status, 
                  user_name, user_email, principal_investigator, collaborator, service_type, sample_type, 
                  organism, reference_genome):
    if n_clicks is None:
        return ""
    
    if not all([location, project_name, user_name]):
        return "Error: Location, Project Name, and User Name are required fields."
    
    os.makedirs(location, exist_ok=True)
    metadata_file = os.path.join(location, f"METADATA_{project_name}.json")
    
    metadata = {
        "Project Name": project_name,
        "Project Description": project_description,
        "Start Date": project_start_date,
        "End Date": project_end_date,
        "Project Size": project_size,
        "Project Status": project_status,
        "User Name": user_name,
        "User Email": user_email,
        "Principal Investigator": principal_investigator,
        "Collaborator": collaborator,
        "Service Type": service_type,
        "Sample Type": sample_type,
        "Organism": organism,
        "Reference Genome": reference_genome
    }
    
    with open(metadata_file, "w") as f:
        json.dump(metadata, f, indent=4)
    
    return f"Metadata saved successfully in {metadata_file}" 

if __name__ == "__main__":
    app.run_server(debug=True)
