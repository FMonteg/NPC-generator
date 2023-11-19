from flask import Blueprint, render_template, request
from pnj_character import PNJ

pnj_bp = Blueprint('pnj', __name__)


@pnj_bp.route('/pnj')
def pnj_gen():
    pnj = PNJ()
    return render_template('pnj_generator.html', title='Générateur de PNJ', character=pnj)

