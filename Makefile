install:
	docker-compose build

up:
	docker-compose up

test: 
	docker-compose run --rm --no-deps --entrypoint "./scripts/tests.sh" flask

lint:
	bash "./scripts/lint.sh"

lint-win:
	"./scripts/lint.sh"