from typing import List

from pyrogram.types import InputMediaDocument

from .types.books_and_documents import Book


# Esta função é usada para gerar o texto ou legenda de um livro.
def create_caption(book: Book) -> str:
	
	caption = ""
	
	if book.title:
		caption += f"**{book.title}**\n\n"
	if book.type:
		caption += f"**Tipo**: __{book.type}__\n"
	if book.category:
		caption += f"**Categoria**: __{book.category}__\n"
	if book.duration:
		caption += f"**Duração**: __{book.duration.human}__\n"
	if book.size:
		caption += f"**Tamanho**: __{book.size.human}__\n"
	if book.author:
		caption += f"**Autor**: __{book.author}__\n"
	if book.narrator:
		caption += f"**Narrador**: __{book.narrator}__\n"
	if book.publisher:
		caption += f"**Editora**: __{book.publisher}__\n"
	if book.views:
		caption += f"**Visualizações**: __{book.views}__\n"
	if book.date:
		caption += f"**Adição**: __{book.date.human}__\n"
	if book.id:
		caption += f"**Identificação**: __{book.id}__\n"
	
	
	return caption


# Este método é usado para criar um grupo de documentos a serem enviados.
def create_media_group(book: Book) -> List[InputMediaDocument]:
	
	group = []
	
	caption = f"**{book.type}**: {book.title}"
	
	for document in book.documents:
		group.append(InputMediaDocument(document.file_id, caption=caption))
	
	return group


		