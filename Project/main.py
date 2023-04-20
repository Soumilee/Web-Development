from flask import Flask
from flask import Blueprint, current_app, render_template, request 
import requests

app = Flask(__name__)
food_recipe = Blueprint('food_recipe', __name__, url_prefix='/',template_folder='templates')

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "0271dcaeefmsh494ffd53ca8f0fcp17c595jsnfb5946b574d5",
  }

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

querystring = {"ingredients":"apples,flour,sugar","number":"5","ignorePantry":"true","ranking":"1"}

headers = {
	"X-RapidAPI-Key": "0271dcaeefmsh494ffd53ca8f0fcp17c595jsnfb5946b574d5",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

querystring = {"tags":"vegetarian,dessert","number":"1"}

headers = {
	"X-RapidAPI-Key": "0271dcaeefmsh494ffd53ca8f0fcp17c595jsnfb5946b574d5",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
response = requests.request("GET", url, headers=headers)

print(response.text)
find = "recipes/findByIngredients"
randomFind = "recipes/random"

@app.route('/')
def search_page():
  pass
  return render_template('search.html')

if __name__ == '__main__':
  app.run()

@app.route('/recipes')
@current_app.cache.cached(timeout=30)
def get_recipes():
  if (str(request.args['ingridients']).strip() != ""):
      # If there is a list of ingridients -> list
      querystring = {"number":"5","ranking":"1","ignorePantry":"false","ingredients":request.args['ingridients']}
      response = requests.request("GET", url + find, headers=headers, params=querystring).json()
      return render_template('recipes.html', recipes=response)
  else:
      # Random recipes
      querystring = {"number":"5"}
      response = requests.request("GET", url + randomFind, headers=headers, params=querystring).json()
      print(response)
      return render_template('recipes.html', recipes=response['recipes'])

@app.route('/recipe')
@current_app.cache.cached(timeout=30)
def get_recipe():
  recipe_id = request.args['id']
  recipe_info_endpoint = "recipes/{0}/information".format(recipe_id)
  ingedientsWidget = "recipes/{0}/ingredientWidget".format(recipe_id)
  equipmentWidget = "recipes/{0}/equipmentWidget".format(recipe_id)

  recipe_info = requests.request("GET", url + recipe_info_endpoint, headers=headers).json()
    
  recipe_headers = {
      'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
      'x-rapidapi-key': "<YOUR_RAPID_API_KEY>",
      'accept': "text/html"
  }
  querystring = {"defaultCss":"true", "showBacklink":"false"}

  recipe_info['inregdientsWidget'] = requests.request("GET", url + ingedientsWidget, headers=recipe_headers, params=querystring).text
  recipe_info['equipmentWidget'] = requests.request("GET", url + equipmentWidget, headers=recipe_headers, params=querystring).text
    
  return render_template('recipe.html', recipe=recipe_info)