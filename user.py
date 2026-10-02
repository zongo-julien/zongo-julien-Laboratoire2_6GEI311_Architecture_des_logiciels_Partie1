"""Classe User - implémentation littérale du diagramme de classes ."""
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ticket import Ticket


class User:
    def __init__(self, userID: int, name: str, email: str, role: str) -> None:
        self.userID: int = userID
        self.name: str = name
        self.email: str = email
        self.role: str = role
        # CHOIX D'IMPLÉMENTATION NON SPÉCIFIÉ PAR LE DIAGRAMME :
        # les associations "User (1) --creates--> Ticket (0..*)" et
        # "User (1) --views--> Ticket (0..*)" sont matérialisées par deux
        # listes de références (extrémités d'association, multiplicité 0..*).
        # Ce ne sont pas des attributs du compartiment de la classe, mais le
        # moyen usuel de traduire une association navigable en code.
        self.createdTickets: list[Ticket] = []
        self.viewedTickets: list[Ticket] = []

    def createTicket(self, ticket: Ticket) -> None:
        # Le ticket est reçu déjà construit (signature du diagramme) :
        # la méthode enregistre le lien "creates".
        self.createdTickets.append(ticket)
        print(f"[User {self.name}] a créé le ticket #{ticket.ticketID} "
              f"('{ticket.title}')")

    def viewTicket(self, ticket: Ticket) -> None:
        
        self.viewedTickets.append(ticket)
        print(f"[User {self.name}] consulte le ticket #{ticket.ticketID} :")
        print(f"    titre       : {ticket.title}")
        print(f"    description : {ticket.description}")
        print(f"    statut      : {ticket.status}")
        print(f"    priorité    : {ticket.priority}")
        print(f"    créé le     : {ticket.creationDate}")
        print(f"    mis à jour  : {ticket.updateDate}")

    def updateTicket(self, ticket: Ticket) -> None:
        # CHOIX D'IMPLÉMENTATION NON SPÉCIFIÉ PAR LE DIAGRAMME :
        # le diagramme ne dit pas quel champ est modifié par updateTicket.
        # La méthode se limite à rafraîchir updateDate et à signaler la mise à jour.
        ticket.updateDate = date.today()
        print(f"[User {self.name}] a mis à jour le ticket #{ticket.ticketID} "
              f"(updateDate = {ticket.updateDate})")
