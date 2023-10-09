from flask import Blueprint, render_template, request
from npc_character import NPC

npc_bp = Blueprint('npc', __name__)


@npc_bp.route('/npc')
def npc_gen():
    npc = NPC()
    return render_template('npc_generator.html', title='NPC Generator', character=npc)

