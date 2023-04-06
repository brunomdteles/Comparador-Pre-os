import httpx
import pandas as pd
from selectolax.parser import HTMLParser
import datetime


today = datetime.date.today()
formatted_date = today.strftime('%d/%m/%Y')

def get_data(store, url, selector, selector_two):
    resp = httpx.get(url, headers={
        "User-Agent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
        },
                     )
    html = HTMLParser(resp.text)
    price = html.css_first(selector).text().strip()
    price = price.replace("€","")
    price = price.replace(" ","")
    price = price.replace("/","")
    price = price.replace("Kg","")
    price = price.replace("un","")
    price = price.replace("\n\n\nkg","")
    price = price.replace("\n\n\n","")
    price = price.replace("\n","")
    
    

    
    name = selector_two
    
    try:
        df = pd.read_excel("preços super.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Data","Loja","Artigo","Preço"])
    new_row = pd.DataFrame([[formatted_date, store, name, price]], columns=df.columns)
    df = df.append(new_row, ignore_index=True)
    df.to_excel("preços super.xlsx", index=False)
    
    return {"Loja": store,"Artigo": name, "Preço":price}

def main():
    results = [
        #Batata
        get_data("Auchan", "https://www.auchan.pt/pt/produtos-frescos/legumes/batatas-alho-e-cebola/batata-vermelha-auchan-3-kg/3483188.html", "span.sales", "Batatas 3Kg"),
        get_data("Continente", "https://www.continente.pt/produto/batata-vermelha-continente-5454736.html?cgid=home", "span.value", "Batatas 3Kg"),
        get_data("Mini-Preço", "https://www.minipreco.pt/produtos/frutas-e-vegetais/vegetais/batatas-aboboras-e-cenouras/p/36778", "span.big-price", "Batatas 3Kg"),
        #Arroz
        get_data("Auchan", "https://www.auchan.pt/pt/alimentacao/mercearia/arroz-e-massa/arroz-agulha-e-carolino/arroz-agulha-cigala-1kg/40299.html", "span.sales", "Arroz Cigala 1Kg"),
        get_data("Continente", "https://www.continente.pt/produto/arroz-agulha-cigala-2305902.html?cgid=home", "span.value", "Arroz Cigala 1Kg"),
        get_data("Mini-Preço", "https://www.minipreco.pt/produtos/mercearia/acompanhamentos/arroz/p/89349", "span.big-price", "Arroz Cigala 1Kg"),
        #Cebola
        get_data("Auchan", "https://www.auchan.pt/pt/produtos-frescos/legumes/batatas-alho-e-cebola/cebola-kg/21946.html", "span.sales", "Cebola 1Kg"),
        get_data("Continente", "https://www.continente.pt/produto/cebola-nova-continente-5063153.html?cgid=home", "span.value", "Cebola 1Kg"),
        get_data("Mini-Preço", "https://www.minipreco.pt/produtos/frutas-e-vegetais/vegetais/alhos-e-cebolas/p/36792", "span.big-price", "Cebola 1Kg")
        ,
        #Maça Gala
        get_data("Auchan", "https://www.auchan.pt/pt/produtos-frescos/fruta/macas-peras-e-uvas/maca-gala-de-alcobaca-igp-auchan-producao-controlada-kg/516485.html", "span.sales", "Maça Gala Alcobaça 1Kg"),
        get_data("Continente", "https://www.continente.pt/produto/maca-gala-igp-alcobaca-continente-3652458.html?cgid=home", "span.value", "Maça Gala Alcobaça 1Kg"),
        get_data("Mini-Preço", "https://www.minipreco.pt/produtos/frutas-e-vegetais/vegetais/alhos-e-cebolas/p/36792", "span.big-price", "Maça Gala Alcobaça 1Kg")
        ,
        #Feijão
        get_data("Auchan", "https://www.auchan.pt/pt/alimentacao/mercearia/conservas/vegetais-secos/feijao-auchan-encarnado-seco-500g/387445.html", "span.sales", "Feijão Encarnado seco 500G"),
        get_data("Continente", "https://www.continente.pt/produto/feijao-vermelho-continente-2733485.html?cgid=home", "span.value", "Feijão Encarnado seco 500G"),
        get_data("Mini-Preço", "https://www.minipreco.pt/produtos/mercearia/acompanhamentos/gr%C3%A3o-e-feij%C3%A3o/p/11657", "span.big-price", "Feijão Encarnado seco 500G")
        ,
        #Leite
        get_data("Auchan", "https://www.auchan.pt/pt/alimentacao/produtos-lacteos/leites/leite-uht/leite-mimosa-uht-meio-gordo-1l/11885.html", "span.sales", "Leite Mimosa Meio Gordo 1L"),
        get_data("Continente", "https://www.continente.pt/pesquisa/?q=leite+meio+gordo+mimosa&start=0&srule=Continente&pmin=0.01", "span.value", "Leite Mimosa Meio Gordo 1L"),
        get_data("Mini-Preço", "https://www.minipreco.pt/produtos/laticinios-e-ovos/leite/leite-meio-gordo-e-gordo/p/6693", "span.big-price", "Leite Mimosa Meio Gordo 1L"),
        get_data("Mercadão", "https://mercadao.pt/store/pingo-doce/product/batata-doce-frita-pingo-doce-150-g", "h2._3MDF8HVHJABdafDgo7eFwa", "Leite Mimosa Meio Gordo 1L")
       ]
    print(results)
if __name__ == "__main__":
    main()
    


