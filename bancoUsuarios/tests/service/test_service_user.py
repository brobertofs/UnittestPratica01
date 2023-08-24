import pytest

from src.service.service_user import ServiceUser


class TestServiceUser:

    @pytest.fixture
    def setup(self):
        # Setup
        service = ServiceUser()
        service.add_user("Fabricio", "Engenheiro")
        yield service

    @pytest.mark.parametrize("name, job, result",
                             [
                                 ("Bruno", "Analista", "SUCCESS: Usuario foi adicionado"),
                                 ("Fabricio", "Engenheiro", "ERROR: Esse usuario existe na lista"),
                                 (000, "Engenheiro", "ERROR: Parametro invalido, deveria ser String"),
                                 (None, "Engenheiro", "ERROR: Parametro invalido, nao pode ser None"),
                             ])
    def test_add_user(self, setup, name, job, result):
        # Setup
        service = setup
        resultado_esperado = result

        # Chamada
        resultado = service.add_user(name, job)

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize("name, result",
                             [
                                 ("Fabricio", "SUCCESS: Usuario foi removido"),
                                 ("Bruno", "ERROR: Esse usuario nao existe na lista"),
                                 (000, "ERROR: Parametro invalido, deveria ser String"),
                                 (None, "ERROR: Parametro invalido, nao pode ser None"),
                             ])
    def test_remove_user(self, setup, name, result):
        # Setup
        service = setup
        resultado_esperado = result

        # Chamada
        resultado = service.remove_user(name)

        # Avalição
        assert resultado == resultado_esperado

    @pytest.mark.parametrize("name, job, result",
                             [
                                 ("Fabricio", "Analista", "SUCCESS: Usuario foi atualizado"),
                                 ("Bruno", "QA", "ERROR: Esse usuario nao existe na lista"),
                                 (000, "QA", "ERROR: Parametro invalido, deveria ser String"),
                                 (None, "QA", "ERROR: Parametro invalido, nao pode ser None"),
                             ])
    def test_update_user(self, setup, name, job, result):
        # Setup
        service = setup
        resultado_esperado = result

        # Chamada
        resultado = service.update_user(name, job)

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize("name, result",
                             [
                                 ("Fabricio", "SUCCESS:"+"\n"+"Nome: Fabricio"+"\n"+"Trabalho: Engenheiro"),
                                 ("Bruno", "ERROR: Esse usuario nao existe na lista"),
                                 (123, "ERROR: Parametro invalido, deveria ser String"),
                                 (None, "ERROR: Parametro invalido, nao pode ser None"),
                             ])
    def test_get_user_name(self, setup, name, result):
        # Setup
        service = setup
        resultado_esperado = result

        # Chamada
        resultado = service.get_user_by_name(name)

        # Avaliação
        assert resultado == resultado_esperado
