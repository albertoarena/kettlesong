# Demo script

A short screen recording (60 to 90 seconds) that shows one full session: greeting, red test, fix, green test, commit, task done. The maintainer records it.

## 1. Prepare the demo project

Create the project in a neutral folder, for example `~/demo/cart`. The folder name shows in the terminal.

`composer.json`:

```json
{
  "name": "demo/cart",
  "type": "project",
  "require": { "php": "^8.3" },
  "require-dev": { "pestphp/pest": "^3.0 || ^4.0" },
  "autoload": { "psr-4": { "App\\": "src/" } },
  "config": { "allow-plugins": { "pestphp/pest-plugin": true } }
}
```

`src/Cart.php` (the loop skips the last item):

```php
<?php

namespace App;

class Cart
{
    /** @var array<int, array{name: string, price: int, qty: int}> */
    private array $items = [];

    public function add(string $name, int $price, int $qty = 1): void
    {
        $this->items[] = ['name' => $name, 'price' => $price, 'qty' => $qty];
    }

    public function total(): int
    {
        $total = 0;

        for ($i = 0; $i < count($this->items) - 1; $i++) {
            $total += $this->items[$i]['price'] * $this->items[$i]['qty'];
        }

        return $total;
    }
}
```

`tests/Unit/CartTest.php`:

```php
<?php

use App\Cart;

it('sums totals', function () {
    $cart = new Cart();
    $cart->add('Seed cake', 10);
    $cart->add('Tea', 5, 2);
    $cart->add('Mushrooms', 10);

    expect($cart->total())->toBe(30);
});
```

Then run:

```bash
printf "vendor/\n" > .gitignore
composer install
./vendor/bin/pest   # 1 failed: expected 30, got 20
git init && git add -A && git commit -m "Initial cart"
```

## 2. Prepare the terminal

- Install the plugin and select the style (see the README). Use the default settings: no `kettlesong.*` lines in `CLAUDE.md`.
- Window size: about 100 columns by 30 rows. Font size: 16 or larger.
- Use a dark theme for the main take. Record a second take with a light theme if time allows.
- Hide personal data: a short shell prompt, no user name, no private paths, no notifications.
- Start a new Claude Code session for each take. The banner shows only on the first greeting.

## 3. Record

Type each prompt exactly. Wait for the full reply before you type the next one.

| # | Prompt | What the viewer sees |
|---|---|---|
| 1 | `Hi` | The green banner, one italic greeting line, a short summary of the project. |
| 2 | `Run the tests with ./vendor/bin/pest` | One italic line about the failure, the exact Pest output, the cause (the loop skips the last item). No art: the banner was in the previous reply. |
| 3 | `Fix it and run the tests again` | The smallest fix in `Cart::total()`, the tests pass, one italic line. The dwarf can appear here. |
| 4 | `Commit it` | A plain commit message with no theme. No art if the previous reply had art. |
| 5 | `Thanks, that's all` | One italic sign-off. The hobbit with tea can appear here. |

## 4. Check each take

- The banner is complete and green.
- Each reply has at most one italic themed line.
- The commit message contains no themed words.
- The dwarf (reply 3) and the hobbit with tea (reply 5) appear.

The replies change from take to take, because Claude writes each line fresh. Art never appears in two replies in a row. Record two or three takes and keep the best one.

## 5. Edit

- Cut the waits while Claude works. Keep the replies at a readable speed.
- Do not add music with lyrics or any audio from the books, films or games.
- End on the hobbit with tea, or on the sign-off line.
