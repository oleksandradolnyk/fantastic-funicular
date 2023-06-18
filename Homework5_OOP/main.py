from flask import Flask, redirect, url_for

from webargs import fields
from webargs.flaskparser import use_kwargs

from database.database_handler import execute_query, formatting_data

app = Flask(__name__)


@app.route('/')
def redirect_from_main():
    return redirect(url_for('tracks_in_hours'))


@app.route("/stats_by_city")
@use_kwargs(
    {
        "genre": fields.Str(load_default=False)
    },
    location="query"
)
def tracks_in_hours(genre):
    keys = [
        "Name",
        "Popularity",
        "City"
    ]
    query = f"""
        SELECT g.Name, COUNT(g.Name) AS Popularity, i.BillingCity
        FROM tracks
        JOIN genres g ON g.GenreId = tracks.GenreId
        JOIN invoice_items ii ON tracks.TrackId = ii.TrackId
        JOIN invoices i ON ii.InvoiceId = i.InvoiceId
        WHERE g.Name = '{genre}'
        GROUP BY i.BillingCity
        ORDER BY Popularity DESC LIMIT 1
            """
    if genre:
        data = execute_query(query)
        if not data:
            return "This genre is not valid or popular anywhere."
    else:
        all_genres = execute_query("SELECT Name from genres")
        return f"Genre is required. Available genres are: {all_genres}"
    formatted_data = formatting_data(keys, data)
    return formatted_data


if __name__ == '__main__':
    app.run(port=5001, debug=True)
