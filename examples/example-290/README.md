# JmesPath support of 'spread' operator

tags: jq, json_query, merge, no_null, spread


* Use *json_query* built-in function *merge* in special case of
  merging selected keys (see Example 2.). Otherwise use *jq* as a
  workaround (see Example 1.). If a key is optional use *not_null*
  (see Example 3.).

* As a side effect this solves the problem of deleting a key by
  JmesPath


## Context. Spread operator.

[JavaScript Demo: Expressions - Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

```
function sum(x, y, z) {
  return x + y + z;
  }

const numbers = [1, 2, 3];

console.log(sum(...numbers));
  // expected output: 6

console.log(sum.apply(null, numbers));
  // expected output: 6
```

## Examples

### Example 1. Workaround using *jq*

See pb1.yml


### Example 2. Special case of merging selected keys

See pb2.yml


### Example 3. If a key is optional use JmesPath built_in function
   *not_null*

See pb3.yml


## References

* [Does JmesPath support something like a spread operator?](https://stackoverflow.com/questions/73479619/does-jmespath-support-something-like-a-spread-operator/73481054#73479619)
* [Ability to set and delete based on a JmesPath #121](https://github.com/jmespath/jmespath.py/issues/121)
