install:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

seed:
	docker-compose run --rm --entrypoint "flask seed" flask

flask:
	docker-compose run --rm --entrypoint "flask $(ARGS)" flask

test:
	docker-compose run --rm --no-deps --entrypoint "./scripts/tests.sh" flask

lint:
	bash "./scripts/lint.sh"

lint-win:
	"./scripts/lint.sh"
