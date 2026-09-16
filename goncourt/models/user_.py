# -*- coding: utf-8 -*-

"""
Classe user_, fille de la classe Person représentant un utilisateur du système goncourt.
"""
from dataclasses import dataclass

from goncourt.models.person import Person


@dataclass
class user_(Person):
    id_user: int
    user_name: str
    password: str
