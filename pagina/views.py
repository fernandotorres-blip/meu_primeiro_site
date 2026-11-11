from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    dados = {
        "nome": "Fernando Torres",
        "idade": 24,
        "altura": 1.60,
        "profissao": "Analista Administrativo, Estudante de programação full stack",
        "cursos": ["Administração", "Programação Full Stack", "Análise de Dados",],
        "hobbies": ["Jogar video game", "Assistir filmes", "Ouvir musicas", "Cinema" "Academia"],
        "cidade": "Recife, PE",
    }
    return render (request, "inicio.html", dados)

def sobre(request):
    return render(request, "sobre.html")
def contato(request):
    return HttpResponse(
        "<hr>"
                "<a href='/'>Início</a> | "
                "<a href='/sobre/'>Sobre</a> | "
                "<a href='/contato/'>Contato</a>"
"<h1>Entre em contato comigo através do contatos abaixo:</h1>"
        "<p>meuemail@exemplo.com</p>"
        "<p>meu numero de telefone: (99) 99999-9999"
        "<p>meu linkdin: a href= https/aodinqwaiofbwaufab.linkdin.com" )
def projetos(request):
    dados = {
        "projetos": ["Calculadora em Python", "Biblioteca com classes", "Meu site em Django"]
    }
    return render(request, "projeto.html", dados)