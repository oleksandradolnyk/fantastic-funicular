import sqlite3

from flask import Flask

from webargs import fields
from webargs.flaskparser import use_kwargs

from database_handler import execute_query, formatting_data

app = Flask(__name__)

@app.route('/order_price')
@use_kwargs(
    {
        "country": fields.Str(load_default=False)
    },
    location="query"
)
def order_price(country):
    keys = [
        "Country",
        "OrderPrice",
    ]
    query = """
            SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice * invoice_items.Quantity) as price
            FROM invoices
            JOIN invoice_items ON invoices.InvoiceId=invoice_items.InvoiceId
            """
    if country:
        query += f"WHERE invoices.BillingCountry = '{country}'"
    query += "GROUP BY invoices.BillingCountry ORDER BY price DESC"
    data = execute_query(query)
    formatted_data = formatting_data(keys, data)
    return formatted_data

@app.route("/tracks")
@use_kwargs(
    {
        "track": fields.Int(load_default=False)
    },
    location="query"
)
def get_all_info_about_track(track):
    keys = [
        "TrackId",
        "TrackName",
        "Composer",
        "Title",
        "Artist_Name",
        "Genre_Name",
        "Media_Type",
        "PlaylistId",
        "Playlist",
        "Milliseconds",
        "UnitPrice",
        "CustomerFirstName",
        "CustomerLastName",
        "CustomerEmail",
        "CustomerCountry"
    ]
    query = """
            SELECT tracks.TrackId, tracks.Name, Composer, Title,
                   artists.Name AS Artist_Name,
                   genres.Name AS Genre_Name,
                   media_types.Name AS Media_Type,
                   playlist_track.PlaylistId,
                   playlists.Name as Playlist,
                   Milliseconds, tracks.UnitPrice, FirstName, LastName, Email, Country
            FROM tracks
            JOIN albums on tracks.AlbumId = albums.AlbumId
            JOIN artists on artists.ArtistId = albums.ArtistId
            JOIN genres on tracks.GenreID = genres.GenreId
            JOIN media_types on tracks.MediaTypeId = media_types.MediaTypeId
            JOIN playlist_track on tracks.TrackId = playlist_track.TrackId
            JOIN playlists on playlist_track.PlaylistId = playlists.PlaylistId
            JOIN invoice_items on tracks.TrackId = invoice_items.TrackId
            JOIN invoices on invoices.InvoiceId = invoice_items.InvoiceId
            JOIN customers on invoices.CustomerId = customers.CustomerId
            """
    if track:
        query += f"WHERE tracks.TrackId='{track}'"
    query += "GROUP BY tracks.TrackId, tracks.Name, playlists.PlaylistId, FirstName, LastName"
    data = execute_query(query)
    formatted_data = formatting_data(keys, data)
    return formatted_data

@app.route("/in_hours")
def tracks_in_hours():
    keys = [
        "Album",
        "TotalHours",
    ]
    query = """
            SELECT albums.Title, ROUND(SUM(Milliseconds) / (1000.0 * 60 * 60), 2) AS TotalHours
            FROM tracks
            JOIN albums ON tracks.AlbumId = albums.AlbumId
            GROUP BY albums.Title
            ORDER BY TotalHours DESC
            """
    data = execute_query(query)
    formatted_data = formatting_data(keys, data)
    return formatted_data

if __name__ == '__main__':
    app.run(port=5001, debug=True)