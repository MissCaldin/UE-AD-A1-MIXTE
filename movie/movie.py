from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType
from flask import Flask, request, jsonify
import json
import resolvers as r

PORT = 3001
HOST = '0.0.0.0'
app = Flask(__name__)

# create elements for Ariadne
type_defs = load_schema_from_path('movie.graphql')
query = QueryType()
movie = ObjectType('Movie')
query.set_field('movie_with_id', r.movie_with_id)
query.set_field('movie_by_title', r.movie_by_title)
schema = make_executable_schema(type_defs, movie, query)
query.set_field('movies', r.all_movies)
schema = make_executable_schema(type_defs, query)
mutation = MutationType()
mutation.set_field('update_movie_rate', r.update_movie_rate)
schema = make_executable_schema(type_defs, movie, query, mutation)
mutation.set_field('add_movie', r.add_movie)
mutation.set_field('delete_movie', r.delete_movie)
schema = make_executable_schema(type_defs, query, mutation)

# root message
@app.route("/", methods=['GET'])
def home():
    return "<h1 style='color:blue'>Welcome to the Movie service!</h1>"

# graphql entry points
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
                        schema,
                        data,
                        context_value=None,
                        debug=app.debug
                    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)