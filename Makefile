.PHONY: install build deploy all clean deploy-if-configured

# Install dependencies
install:
	npm install

validate:
	python3 scripts/check_translation.py

fix:
	python3 scripts/fix_translation.py --fix

# Build the project (output will be in ./dist)
build: validate
	npm run build

# Deploy to Cloudflare Pages
# Note: Ensure you are logged in via 'npx wrangler login'
deploy: build
	rm -rf .wrangler/deploy
	npx wrangler pages deploy dist --project-name weekly
	
dev:
	npm run dev

# Clean build artifacts
clean:
	rm -rf dist .wrangler/deploy
