from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, filters, ConversationHandler, CallbackQueryHandler, ContextTypes, ApplicationBuilder

import asyncio

# Estados para o ConversationHandler
TERMO, NOME, CONFIRMA_NOME, MENU, SUGESTAO_DISCUSSAO = range(5)


# Função para criar botão de voltar ao menu
def botao_voltar_menu():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Voltar ao Menu", callback_data="voltar_menu")]])


# Função de início
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Aceitar", callback_data='aceitar')],
        [InlineKeyboardButton("Recusar", callback_data='recusar')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Bem-vindo ao Chat da FURIA! ⚡\n\nPara continuar, por favor, aceite os termos do chat.\n\n"
        "Este é um chat desenvolvido para um desafio prático e pode conter erros e bugs. "
        "Algumas notícias podem ser fictícias e estarem desatualizadas dependendo do dia em que você acessar o chat.\n\n"
        "Escolha uma das opções abaixo:",
        reply_markup=reply_markup
    )
    return TERMO


# Aceitação dos termos
async def aceitar_termos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'aceitar':
        await query.edit_message_text("Obrigado por aceitar os termos! Vamos começar. 😊")
        await query.message.reply_text("Qual é o seu nome?")
        return NOME
    elif query.data == 'recusar':
        await query.edit_message_text("Obrigado! Esperamos ver você novamente em breve. 👋")
        return ConversationHandler.END


# Captura do nome
def botao_confirmar_nome():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Sim", callback_data='sim')],
        [InlineKeyboardButton("Não", callback_data='nao')]
    ])


async def capturar_nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.message.text
    context.user_data['nome'] = nome
    await update.message.reply_text(
        f"Seu nome é {nome}? Se estiver correto, clique em 'Sim' ou em 'Não' para corrigir.",
        reply_markup=botao_confirmar_nome()
    )
    return CONFIRMA_NOME


# Confirmação do nome
async def confirmar_nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'sim':
        await query.edit_message_text("Perfeito! Vamos para o menu principal.")
        return await resposta_menu(update, context)
    elif query.data == 'nao':
        await query.edit_message_text("Por favor, digite seu nome corretamente.")
        return NOME


# Menu principal
async def resposta_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Canal de Notícias", callback_data='1')],
        [InlineKeyboardButton("Acompanhar Jogos ao Vivo", callback_data='2')],
        [InlineKeyboardButton("Calendário de Jogos", callback_data='3')],
        [InlineKeyboardButton("Discussões de Jogos", callback_data='4')],
        [InlineKeyboardButton("Eventos e Encontros", callback_data='5')],
        [InlineKeyboardButton("Espaço para Novos Fãs", callback_data='6')],
        [InlineKeyboardButton("Loja da FURIA", callback_data='7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        await update.callback_query.message.reply_text("Escolha uma opção do menu:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Escolha uma opção do menu:", reply_markup=reply_markup)
    return MENU


# Voltar ao menu
async def voltar_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    return await resposta_menu(update, context)


# Canal de notícias
async def canal_noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    resposta = "🔥 Canal de Notícias da FURIA CS:\n\n"
    resposta += "Aqui você encontra as últimas novidades sobre o time e os resultados de jogos.\n\n"
    resposta += "📰 Portal de notícias: https://themove.gg\n\n"
    resposta += "🧑‍💻 Jogadores atuais:\n\n"
    resposta += "🌎 Time: CS Internacional\n"
    resposta += "Kaike 'KSCERATO' Cerato - 2018\n"
    resposta += "Gabriel 'FalleN' Toledo - 2023\n"
    resposta += "Danil 'molodoy' Golubenko - 2025\n"
    resposta += "Yuri 'yuurih' Santos - 2017\n"
    resposta += "Mareks 'YEKINDAR' Gajinskis - Stand-in 2025\n"
    resposta += "Sidnei 'sidde' Macedo - 2024\n\n"
    resposta += "👩🎮 Time: CS Feminino\n"
    resposta += "Izabella 'izaa' Galle - 2020\n"
    resposta += "Karina 'kaah' Takahashi - 2020\n"
    resposta += "Gabriela 'gabs' Freindorfer - 2020\n"
    resposta += "Bruna 'bizinha' Marvila - 2024\n"
    resposta += "Lucía 'lulitenz' Dubra - 2024\n\n"
    resposta += "💬 Últimos resultados dos jogos\n"
    resposta += "Quarta-feira, 9 de Abril de 2025 às 09:50 -> FURIA vs The MongolZ | Resultado - FURIA 0 e The MongolZ 2 | Vitória = The MongolZ\n\n"
    resposta += "Terça-feira, 8 de Abril de 2025 às 06:05 -> FURIA vs Virtus.pro | Resultado - FURIA 0 e Virtus.pro 2 | Vitória = Virtus.pro\n\n"
    resposta += "Segunda-feira, 7 de Abril de 2025 às 11:05 -> FURIA vs Complexity | Resultado - FURIA 1 e Complexity 2 | Vitória = Complexity\n\n"
    await query.edit_message_text(resposta, reply_markup=botao_voltar_menu())
    return MENU


# Jogos ao vivo (Simulação)
async def acompanhar_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    mensagens = [
        "🎮 Partida em andamento: FURIA vs The MongolZ",
        "🔹 1º mapa: Mirage - FURIA lidera por 12-6",
        "💥 Destaque: KSCERATO com 21 eliminações!",
        "🔥 A FURIA está perto da vitória, vamos torcer juntos! #GoFURIA",
        "⚡ Depois de uma reviravolta inacreditável The MongolZ acaba vencendo essa rodada."
    ]
    await query.edit_message_text(mensagens[0])
    for msg in mensagens[1:-1]:
        await asyncio.sleep(3)
        await query.message.reply_text(msg)
    await asyncio.sleep(3)
    await query.message.reply_text(mensagens[-1], reply_markup=botao_voltar_menu())
    return MENU


# Calendário
async def calendario_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    calendario = "🗓️ 05/05/2025 - FURIA vs NAVI - IEM Katowice\n\n"
    calendario += "🗓️ 10/05/2025 - FURIA vs Vitality - Roobet Cup\n\n"
    calendario += "🗓️ 15/05/2025 - FURIA vs paiN Gaming - ESL Challenger\n\n"
    calendario += "🗓️ 22/05/2025 - FURIA vs Imperial - Pinnacle Cup\n\n"
    calendario += "🗓️ 28/05/2025 - FURIA vs MIBR - BGS Esports\n\n"
    await query.edit_message_text(calendario, reply_markup=botao_voltar_menu())
    return MENU


# Discussões
async def discussao_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("🧠 Envie sua sugestão de discussão sobre o time ou táticas:")
    return SUGESTAO_DISCUSSAO


# Eventos
async def eventos_encontros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    eventos = "📺 06/05/2025 - Watch Party: FURIA vs NAVI às 18h (via Discord da comunidade)\n\n"
    eventos += "🎉 12/05/2025 - Bate-papo pós-jogo com convidados especiais\n\n"
    eventos += "🔥 20/05/2025 - Sessão de perguntas e respostas com ex-jogadores da FURIA\n\n"
    eventos += "👥 25/05/2025 - Encontro virtual para novos fãs conhecerem a história do time\n\n"
    await query.edit_message_text(eventos, reply_markup=botao_voltar_menu())
    return MENU


# Espaço para novos fãs
async def espaco_novos_fas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    mensagem = "👋 Bem-vindo ao Espaço para Novos Fãs da FURIA!\n\n"
    mensagem += "Aqui você pode aprender mais sobre a história, jogadores e como participar da comunidade. "
    mensagem += "Siga a FURIA nas redes sociais para ficar sempre por dentro:\n\n"
    mensagem += "🌐 Site Oficial: https://www.furia.gg\n\n"
    mensagem += "📰 Portal de Notícias: https://themove.gg\n\n"
    mensagem += "📸 Instagram: https://www.instagram.com/furiagg/\n\n"
    mensagem += "🐦 Twitter/X: https://x.com/FURIA\n\n"
    mensagem += "🎥 YouTube: https://www.youtube.com/furiagg\n\n"
    mensagem += "📺 Twitch: https://www.twitch.tv/furiatv\n\n"
    mensagem += "💬 Canal do WhatsApp: https://whatsapp.com/channel/0029VakQdaDDp2QDOr5jgi2F\n\n"
    mensagem += "📘 Facebook: https://www.facebook.com/furiagg\n\n\n"
    mensagem += "Explore, interaja e venha torcer com a gente! 🎮🔥"
    await query.edit_message_text(mensagem, reply_markup=botao_voltar_menu())
    return MENU


# Loja
async def loja_furia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "🛍️ Confira os produtos oficiais da FURIA na loja online!\n\n"
        "Acesse agora: https://www.furia.gg\n\n"
        "Vista a camisa e mostre que é #FURIA até o fim! 💥",
        reply_markup=botao_voltar_menu()
    )
    return MENU


# Sugestão de discussão
async def receber_sugestao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Obrigado pela sugestão! Sua opinião é importante para a equipe FURIA.", reply_markup=botao_voltar_menu())
    return MENU


# Função principal
def main():
    application = ApplicationBuilder().token('USAR TOKEN AQUI').build()

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            TERMO: [CallbackQueryHandler(aceitar_termos)],
            NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, capturar_nome)],
            CONFIRMA_NOME: [CallbackQueryHandler(confirmar_nome)],
            MENU: [
                CallbackQueryHandler(canal_noticias, pattern='^1$'),
                CallbackQueryHandler(acompanhar_jogos, pattern='^2$'),
                CallbackQueryHandler(calendario_jogos, pattern='^3$'),
                CallbackQueryHandler(discussao_jogos, pattern='^4$'),
                CallbackQueryHandler(eventos_encontros, pattern='^5$'),
                CallbackQueryHandler(espaco_novos_fas, pattern='^6$'),
                CallbackQueryHandler(loja_furia, pattern='^7$'),
                CallbackQueryHandler(voltar_menu, pattern='^voltar_menu$'),
            ],
            SUGESTAO_DISCUSSAO: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_sugestao)],
        },
        fallbacks=[],
    )

    application.add_handler(conversation_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
