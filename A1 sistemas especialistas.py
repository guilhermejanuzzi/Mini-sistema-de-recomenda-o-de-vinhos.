import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
FACTS = {
    "peixe": {
        "categoria":"peixe",
        "gordura": "baixa",
        "sabor": "delicado",
        "exemplos": ["salmão", "tilápia", "bacalhau", "camarão"],
        "vinhos": ["Sauvignon Blanc", "Vinho Verde", "Champagne (brut)", "Espumante seco."]
    }
    ,
    "frango": {
        "categoria": "carne_branca",
        "gordura": "média",
        "sabor": "suave",
        "exemplos": ["frango"],
        "vinhos": ["Chardonnay leve", "Pinot Noir leve", "Chenin Blanc."]
    },
    "file_mignon": {
        "categoria": "carne_vermelha_magra",
        "gordura": "baixa",
        "sabor": "médio",
        "exemplos": ["filé mignon", "lagarto"],
        "vinhos": ["Merlot", "Malbec jovem", "Tempranillo."]
    },
    "picanha": {
        "categoria": "carne_vermelha_gorda",
        "gordura": "alta",
        "sabor": "intenso",
        "exemplos": ["picanha", "costela"],
        "vinhos": ["Cabernet Sauvignon", "Syrah", "Tannat", "Zinfandel."]
    }
}

CATEGORY_TO_FACT_KEY = {
    "peixe": "peixe",
    "carne_branca": "frango",
    "carne_vermelha_magra": "file_mignon",
    "carne_vermelha_gorda": "picanha"
}

rules = [
    {
        "name": "carne_vermelha_gorda",
        "condition": lambda f: f.get("gordura") == "alta" or f.get("categoria") == "carne_vermelha_gorda",
        "action": "Tintos encorpados e tânicos (ex: Cabernet Sauvignon, Syrah)"
    },
    {
        "name": "peixe",
        "condition": lambda f: f.get("categoria") == "peixe",
        "action": "Vinhos brancos leves ou espumantes (ex: Sauvignon Blanc, Vinho Verde, Champagne/brut)"
    },
    {
        "name": "carne_branca",
        "condition": lambda f: f.get("categoria") == "carne_branca",
        "action": "Vinho branco encorpado ou tinto leve (ex: Chardonnay, Pinot Noir leve)"
    },
    {
        "name": "carne_vermelha_magra",
        "condition": lambda f: f.get("categoria") == "carne_vermelha_magra",
        "action": "Tintos de corpo médio (ex: Merlot, Malbec)"
    }
]
def inferir_recomendacao(fact):
    if not fact or not isinstance(fact, dict):
        return "Tipo de carne desconhecido. Tente novamente."

    vinhos = fact.get("vinhos", [])
    if vinhos:
        return f"{', '.join(vinhos)}"
    else:
        return "Nenhuma recomendação de vinhos disponível."     
    
def get_fact_for_category(category):
    key = CATEGORY_TO_FACT_KEY.get(category)
    if key and key in FACTS:
        return FACTS[key]
    return {"categoria": category, "gordura": "desconhecida", "sabor": "desconhecido", "exemplos":[]}

def main_loop():
    
    while (True):
        clear_console()
        print("\nBem-vindo ao Harmonize Vinho! (Motor de Inferência)\n")
        comecar = input("Gostaria de começar? (digite 'sim' para começar ou 'sair' para encerrar): ").strip().lower()

        if comecar == "sair":
            print("\nAté a próxima!")
            break

        if comecar != "sim":
            print("Entrada não reconhecida. Voltando ao menu.")
            time.sleep(2)
            continue

        print("\nQual tipo de carne você gostaria de preparar?\n")
        print("1 - Peixe")
        print("2 - Carne branca")
        print("3 - Carne vermelha magra")
        print("4 - Carne vermelha gorda\n")
        
        while True:
            try:
                tipo_escolhido = int(input("Opção escolhida (1-4): "))
                if tipo_escolhido not in (1, 2, 3, 4):
                    print("Erro: escolha um número entre 1 e 4.")
                    continue
                break
            except ValueError:
                print("Erro: digite apenas números.")

        categoria_map = {
            1: "peixe",
            2: "carne_branca",
            3: "carne_vermelha_magra",
            4: "carne_vermelha_gorda"
        }

        categoria = categoria_map[tipo_escolhido]
        
        fact = get_fact_for_category(categoria)
        print(f"\n Carne escolhida: {categoria}")
        print(f"   Características -> gordura: {fact.get('gordura')}, sabor: {fact.get('sabor')}")
        if fact.get("exemplos"):
            print(f"   Exemplos: {', '.join(fact.get('exemplos'))}")
        recomendacao = inferir_recomendacao(fact)
        print(f"\n Recomendação: {recomendacao}")

        input("\nPressione Enter para retornar ao menu...")

if __name__ == "__main__":
    main_loop()