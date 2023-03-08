from database import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()
pokemons = db.collection.find()
for pokemon in pokemons:
    print(pokemon)

def getPokemonByDex(number:int):
    return db.collection.find({"id": number})

bulbasaur = getPokemonByDex(1)
writeAJson(bulbasaur, "bulbassaur")


def getPokemonByHP(number:int):
    return db.collection.find({"base.HP":number})

vida = getPokemonByHP(80)
writeAJson(vida, "vida")


def getPokemonbyAttack(number:int):
    return db.collection.find(({"base.Attack": {"$lte":number}}))

ataque =  getPokemonbyAttack(10)
writeAJson(ataque, "ataque")


def getPokemonbySpeed(number:int):
    return db.collection.find({"base.Speed":number})

rapidez = getPokemonbySpeed(20)
writeAJson(rapidez, "rapidez")


def getPokemonbyDefense(number:int):
    return db.collection.find({"base.Defense":number})

defesa = getPokemonbyDefense(50)
writeAJson(defesa,"defesa")