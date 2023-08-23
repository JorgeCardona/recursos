import random

def generar_muestra(tamano):
    
    nombres = [
    "Cecilia", "Emma", "Olivia", "Ava", "Isabella", "Mia", "Zoe", "Lily", "Emily", "Chloe",
    "Layla", "Madison", "Madelyn", "Abigail", "Aubrey", "Charlotte", "Amelia", "Ella", "Kaylee", "Avery",
    "Aaliyah", "Hailey", "Hannah", "Addison", "Riley", "Harper", "Aria", "Arianna", "Mackenzie", "Lila",
    "Evelyn", "Adalyn", "Grace", "Brooklyn", "Ellie", "Anna", "Kaitlyn", "Isabelle", "Sophie", "Scarlett",
    "Nathalie", "Leah", "Sarah", "Nora", "Mila", "Elizabeth", "Lillian", "Kylie", "Audrey", "Lucy",
    "Maya", "Angela", "Makayla", "Gabriela", "Elena", "Victoria", "Tatiana", "Savannah", "Peyton", "Maria",
    "Grace", "Hailey", "Aubrey", "Ariana", "Leila", "Paisley", "Alyssa", "Claire", "Camila", "Sophie",
    "Lucia", "Lilly", "Scarlett", "Jasmine", "Morgan", "Nevaeh", "Sofia", "Zoey", "Addison", "Eva",
    "Skyler", "Ellie", "Trinity", "Leah", "Zoe", "Kylie", "Ana", "Lila", "Brooke", "Bailey",
    "Maria", "Rachel", "Aria", "Payton", "Reagan", "Harper", "Kristin", "Gianna", "Brianna", "Diana"
    ]

    regiones = ["Africa", "America", "Asia", "Europa", "Oceania"]
    profesiones = ["Médica", "Ingeniera", "Profesora", "Abogada", "Arquitecta", "Diseñadora", "Psicóloga", "Periodista", "Veterinaria", "Economista", "Chef", "Científica", "Pilota", "Escritora", "Programadora", "Astrónoma", "Fotógrafa", "Traductora", "Investigadora", "Artista"]
    hobbies = ["Leer", "Pintar", "Bailar", "Correr", "Nadar", "Escribir", "Viajar", "Cine", "Musica", "Fotografía"]


    labels = ['nombre', 'profesion', 'salario', 'hobbie', 'region']
    muestra = []
    for _ in range(tamano):
        nombre = random.choice(nombres)
        salario = random.randint(8000, 12000)
        profesion = random.choice(profesiones)
        hobbie = random.choice(hobbies)
        region = random.choice(regiones)
        
        
        tupla = (nombre, profesion, salario, hobbie, region)
        muestra.append(tupla)
    
    return muestra, labels