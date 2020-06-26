# Generate api-clients

This folder contains code to transform the api-specifications into api-clients.  We're focusing on python and R for our data scientists.

This is the code to generate these libraries based on the api-specifications.

    APIDIR=`pwd`

    docker run -it -v $APIDIR:$APIDIR openlattice/openapi-generator-cli generate -i $APIDIR/rundeck.yaml -g python -o $APIDIR/python -c $APIDIR/oas-config.json

    docker run -it -v $APIDIR:$APIDIR openlattice/openapi-generator-cli generate -i $APIDIR/rundeck.yaml -g r -o $APIDIR/R -c $APIDIR/oas-config.json


