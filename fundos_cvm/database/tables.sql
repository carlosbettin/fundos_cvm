
CREATE TABLE fi_diario
    (
        fundo_id PRIMARY KEY FOREIGN KEY,
        dt_comptc DATE,
        vl_total NUMERIC(17, 2),
        vl_cota NUMERIC(27, 12),
        vl_patrim_liq NUMERIC(17, 2),
        captc_dia NUMERIC(17, 2),
        resg_dia NUMERIC(17, 2),
        nr_cotst INT(10)
    )


CREATE TABLE fi_cadastro
    (
        fundo_id PRIMARY KEY FOREIGN KEY,
        cnpj_fundo VARCHAR(20),
        den_social VARCHAR(100),
        sit VARCHAR(40),
        dt_ini_ativ DATE(),
        classe varchar(100),
        condom varchar(15),
        diretor varchar(100),
        admin varchar(100),
        gestor varchar(20),
        auditor varchar(100),
    )


CREATE TABLE fi_extrato
    (
        fundo_id INT IDENTITY(1, 1) PRIMARY KEY,
        cnpj_fundo VARCHAR(20),
        den_social VARCHAR(100),
        dt_comptc DATE,
        condom VARCHAR(7),
        prazo VARCHAR(200),
        publico_alvo VARCHAR(26),
        classe_anbima VARCHAR(51),
        distrib VARCHAR(76),
        polit_invest VARCHAR(24),
        aplic_min VARCHAR(15),
        qt_dia_conversao_cota INT(10),
        qt_dia_pagto_cota INT(10),
        qt_dia_resgate_cotas INT(10),
        qt_dia_pgto_resgate INT(10),
        tp_dia_pgto_resgate INT(13),
        taxa_saida_pagto_resgate VARCHAR(1),
        taxa_adm DECIMAL(15, 6),
        taxa_custodia_maxima DECIMAL(15, 6),
        existe_taxa_perf VARCHAR(1),
        taxa_perf NUMERIC(27, 12),
        param_taxa_perf VARCHAR(50),
        pr_indice_refer_taxa_perf NUMERIC(27, 12),
        vl_cupom NUMERIC(27, 12),
        calc_taxa_perfm VARCHAR(7),
        inf_taxa_perf VARCHAR(400),
    )
