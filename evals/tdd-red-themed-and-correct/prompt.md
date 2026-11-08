---
description: "tdd-red-themed-and-correct"
tags: ["voice", "tdd"]
plugins: ["../../harness"]
max_turns: 5
---

Pest output:
FAILED Tests\Unit\CartTest > it sums totals
Expected 30, got 20.

public function total(): int {
    $sum = 0;
    for ($i = 0; $i < count($this->items) - 1; $i++) {
        $sum += $this->items[$i]->price;
    }
    return $sum;
}
What is wrong?
