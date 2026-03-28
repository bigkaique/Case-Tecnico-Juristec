Inicialmente, procuraria identificar a razão pela qual a tabela sumiu do código HTML. O fato de levar alguns segundos para surgir no navegador sugere que os dados estão sendo inseridos via JavaScript. Como o Requests não processa JavaScript, ele não consegue acessar essas informações.

Para investigar, inspecionaria o site no navegador, usando as Ferramentas de Desenvolvedor (F12), na aba "Rede", para verificar se há alguma chamada (API) buscando os dados da tabela. Se identificar essa chamada, tentaria usar o Requests diretamente nessa API, por ser uma solução mais direta e ágil.

Se não encontrar uma API, recorreria a ferramentas que emulam um navegador, como o Selenium, que aguarda o carregamento completo da página antes de extrair os dados.

Quanto ao erro 403, ele surge porque o site provavelmente identificou múltiplas solicitações consecutivas e barrou o acesso.

Para contornar isso, experimentaria algumas táticas fáceis:

inserir um User-Agent nas requisições para imitar um navegador real
adicionar um tempo de espera (delay) entre as requisições para aliviar a carga no site
implementar tratamento de erro para evitar diversas tentativas seguidas

Se ainda assim não resolver, pesquisaria se o site possui alguma proteção mais robusta (como bloqueio por IP) e evitaria o excesso de requisições em sequência.