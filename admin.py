"""Classe Admin - implémentation littérale du diagramme de classes ."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ticket import Ticket
    from user import User


class Admin:
    def __init__(self, adminID: int, name: str, email: str) -> None:
        self.adminID: int = adminID
        self.name: str = name
        self.email: str = email
        # CHOIX D'IMPLÉMENTATION NON SPÉCIFIÉ PAR LE DIAGRAMME :
        # les associations "Admin (1) --assigns--> Ticket (0..*)" et
        # "Admin (1) --closes--> Ticket (0..*)" sont matérialisées par deux
        # listes de références (extrémités d'association, multiplicité 0..*).
        self.assignedTickets: list[Ticket] = []
        self.closedTickets: list[Ticket] = []

    def assignTicket(self, ticket: Ticket, user: User) -> None:
        # CHOIX D'IMPLÉMENTATION NON SPÉCIFIÉ PAR LE DIAGRAMME :
        # Admin.assignTicket délègue à Ticket.assignTo(user) (le diagramme
        # ne précise pas ce lien d'appel).
        self.assignedTickets.append(ticket)
        print(f"[Admin {self.name}] assigne le ticket #{ticket.ticketID} "
              f"à {user.name}")
        ticket.assignTo(user)

    def closeTicket(self, ticket: Ticket) -> None:
        # CHOIX D'IMPLÉMENTATION NON SPÉCIFIÉ PAR LE DIAGRAMME :
        # la fermeture est réalisée via Ticket.updateStatus("Fermé") ;
        # la valeur exacte du statut de fermeture n'est pas définie dans le
        # diagramme (status est un simple str).
        self.closedTickets.append(ticket)
        print(f"[Admin {self.name}] ferme le ticket #{ticket.ticketID}")
        ticket.updateStatus("Fermé")

    def viewAllTickets(self) -> list[Ticket]:
        # CHOIX D'IMPLÉMENTATION NON SPÉCIFIÉ PAR LE DIAGRAMME :
        # le diagramme ne contient aucun dépôt global de tickets. La méthode
        # retourne donc les tickets liés à cet admin par ses associations
        # "assigns" et "closes" (sans doublon, ordre d'apparition conservé).
        tous: list[Ticket] = []
        for t in self.assignedTickets + self.closedTickets:
            if t not in tous:
                tous.append(t)
        print(f"[Admin {self.name}] consulte tous les tickets "
              f"({len(tous)} ticket(s))")
        return tous
