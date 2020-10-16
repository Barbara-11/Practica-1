#!/bin/bash
$curl1 = curl -s ["https://api.github.com/users/defunk"] | sh
$curl2 = curl -s ["-i https://api.github.com/users/defunkt"] | sh
$curl3 = curl -s ["-i https://api.github.com/repos/twbs/bootstrap"] | sh

