"""Classe Ticket - implémentation littérale du diagramme de classes."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

# Import uniquement pour les annotations de type : évite l'import circulaire
# entre ticket.py et utilisateur.py (Ticket <-> User).
if TYPE_CHECKING:
    from user import User


class Ticket:
    def __init__(
        self,
        ticketID: int,
        title: str,
        description: str,
        status: str,
        priority: str,
        creationDate: date,
        updateDate: date,
    ) -> None:
        self.ticketID: int = ticketID
        self.title: str = title
        self.description: str = description
        self.status: str = status          # simple str, aucune validation de transition
        self.priority: str = priority
        self.creationDate: date = creationDate
        self.updateDate: date = updateDate

    def assignTo(self, user: User) -> None:
        # REMARQUE : le diagramme ne prévoit aucun attribut pour mémoriser
        # l'utilisateur assigné (ex. "assignee"). Conformément aux contraintes,
        # aucun attribut n'est ajouté : la méthode se contente d'afficher
        # l'assignation et de rafraîchir la date de mise à jour.
        # CHOIX D'IMPLÉMENTATION NON SPÉCIFIÉ PAR LE DIAGRAMME :
        # updateDate est mis à la date du jour lors de l'assignation.
        self.updateDate = date.today()
        print(f"[Ticket #{self.ticketID}] assigné à l'utilisateur "
              f"{user.name} (userID={user.userID})")

    def updateStatus(self, status: str) -> None:
        # Aucune validation de transition : le nouveau statut est accepté tel quel.
        ancien = self.status
        self.status = status
        # CHOIX D'IMPLÉMENTATION NON SPÉCIFIÉ PAR LE DIAGRAMME :
        # updateDate est mis à la date du jour lors du changement de statut.
        self.updateDate = date.today()
        print(f"[Ticket #{self.ticketID}] statut : '{ancien}' -> '{self.status}'")

    def addComment(self, comment: str) -> None:
        # REMARQUE : le diagramme ne prévoit aucun attribut pour stocker les
        # commentaires (ex. liste "comments"). Aucun attribut n'est ajouté :
        # le commentaire est seulement affiché.
        # CHOIX D'IMPLÉMENTATION NON SPÉCIFIÉ PAR LE DIAGRAMME :
        # updateDate est mis à la date du jour lors de l'ajout d'un commentaire.
        self.updateDate = date.today()
        print(f"[Ticket #{self.ticketID}] commentaire ajouté : \"{comment}\"")
