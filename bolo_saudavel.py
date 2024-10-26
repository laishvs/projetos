# Aula Git - Laís Hrynjcysyn Venâncio dos Santos
# Receita de Bolo Saudável de Banana com Nozes e Canela

# Passo 1: Definir os ingredientes
def ingredientes():
    ingredientes = {
        "bananas maduras": 3,  # Bananas bem maduras
        "ovos": 2,              # Ovos
        "aveia em flocos": 1,   # 1 xícara de aveia
        "mel ou adoçante": 1,   # 1/2 xícara de mel ou a gosto
        "nozes picadas": 1/2,    # 1/2 xícara de nozes
        "canela em pó": 1,      # 1 colher de sopa de canela
        "fermento em pó": 1,     # 1 colher de chá de fermento
        "sal": 1/4               # Uma pitada de sal
    }
    return ingredientes

# Passo 2: Preparo
def preparar_ingredientes(ingredientes):
    print("\nPreparando os ingredientes:")
    for ingrediente, quantidade in ingredientes.items():
        print(f"{quantidade} de {ingrediente}")

# Passo 3: Preparo da massa
def preparar_massa(ingredientes):
    print("\nPreparando a massa do bolo...")
    
    # 1. Amasse as bananas
    print("1. Amasse as bananas em uma tigela grande.")
    
    # 2. Adicione os ovos e misture bem
    print("2. Adicione os ovos às bananas amassadas e misture bem.")
    
    # 3. Adicione o mel ou adoçante
    print("3. Adicione o mel (ou adoçante) e misture novamente.")
    
    # 4. Adicione a aveia
    print("4. Adicione a aveia e misture até ficar homogêneo.")
    
    # 5. Adicione as nozes, canela, fermento e sal
    print("5. Adicione as nozes picadas, canela, fermento em pó e sal. Misture tudo.")

# Passo 4: Assar o bolo
def assar_bolo():
    print("\nPreparando para assar o bolo...")
    print("1. Preaqueça o forno a 180°C (350°F).")
    print("2. Unte uma forma com manteiga ou óleo.")
    print("3. Despeje a massa do bolo na forma.")
    print("4. Asse por cerca de 30-40 minutos ou até que um palito saia limpo.")
    print("5. Deixe esfriar antes de desenformar.")

# Passo 5: Finalização
def finalizacao():
    print("\nO bolo saudável de banana com nozes e canela está pronto!")

# Função principal para executar a receita
def receita_bolo_banana():
    ingredientes = ingredientes()
    preparar_ingredientes(ingredientes)
    preparar_massa(ingredientes)
    assar_bolo()
    finalizacao()

# Executar a receita
receita_bolo_banana()
