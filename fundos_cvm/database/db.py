from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FundCvm555(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'))
	isin = db.Column(db.String(12), index=True, unique=True)
	cnpj_fundo = db.Column(db.String(30), unique=True)
	nome_gestor = db.Column(db.String(150))
	diretor_gestor = db.Column(db.String(150))
	tx_adm = db.Column(db.Numeric(8,6))
	tx_adm_max = db.Column(db.Numeric(8,6))
	tx_perf = db.Column(db.Numeric(8,6))
	tx_perf_idx = db.Column(db.Integer, db.ForeignKey('assets.id'))
	# res_cota_valor
	
class fi_cadastro(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	cnpj_fundo = db.Column(db.String(30), unique=True)
	den_social = db.Column(db.String(100), unique=True)
	sit = db.Column(db.String(30))
	dt_init_ativ = db.Column(db.DateTime)
	# classe
	condom = db.Column(db.String(15))
	diretor = db.Column(db.String(100))
	admin = db.Column(db.String(100))
	gestor = db.Column(db.String(100))
	auditor = db.Column(db.String(100))