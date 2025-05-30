SCHEMA = {
  "typeName" : "AWS::OpenSearchServerless::Index",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-opensearchserverless",
  "description" : "An OpenSearch Serverless index resource",
  "tagging" : {
    "taggable" : False
  },
  "definitions" : {
    "IndexSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Index" : {
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "RefreshInterval" : {
              "type" : "string",
              "description" : "How often to perform refresh operation (e.g. '1s', '5s')"
            },
            "Knn" : {
              "type" : "boolean",
              "description" : "Enable/disable k-nearest neighbor search capability"
            },
            "KnnAlgoParamEfSearch" : {
              "type" : "integer",
              "description" : "Size of the dynamic list for the nearest neighbors"
            }
          }
        }
      }
    },
    "PropertyMapping" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Dimension" : {
          "type" : "integer",
          "description" : "Dimension size for vector fields, defines the number of dimensions in the vector"
        },
        "Index" : {
          "type" : "boolean",
          "description" : "Whether a field should be indexed"
        },
        "Method" : {
          "type" : "object",
          "description" : "Configuration for k-NN search method",
          "additionalProperties" : False,
          "properties" : {
            "Engine" : {
              "type" : "string",
              "enum" : [ "nmslib", "faiss", "lucene" ],
              "description" : "The k-NN search engine to use"
            },
            "Name" : {
              "type" : "string",
              "description" : "The algorithm name for k-NN search",
              "enum" : [ "hnsw", "ivf" ]
            },
            "SpaceType" : {
              "type" : "string",
              "description" : "The distance function used for k-NN search",
              "enum" : [ "l2", "l1", "linf", "cosinesimil", "innerproduct", "hamming" ]
            },
            "Parameters" : {
              "type" : "object",
              "description" : "Additional parameters for the k-NN algorithm",
              "additionalProperties" : False,
              "properties" : {
                "EfConstruction" : {
                  "type" : "integer",
                  "minimum" : 1,
                  "description" : "The size of the dynamic list used during k-NN graph creation"
                },
                "M" : {
                  "type" : "integer",
                  "description" : "Number of neighbors to consider during k-NN search",
                  "minimum" : 2,
                  "maximum" : 100
                }
              }
            }
          },
          "required" : [ "Name", "Engine" ]
        },
        "Properties" : {
          "type" : "object",
          "description" : "Nested fields within an object or nested field type",
          "additionalProperties" : False,
          "patternProperties" : {
            "^[A-Za-z0-9_.-]{1,64}$" : {
              "$ref" : "#/definitions/PropertyMapping",
              "description" : "Nested field name and its mapping configuration"
            }
          }
        },
        "Type" : {
          "type" : "string",
          "description" : "The field data type. Must be a valid OpenSearch field type.",
          "enum" : [ "text", "knn_vector" ]
        },
        "Value" : {
          "type" : "string",
          "description" : "Default value for the field when not specified in a document"
        }
      },
      "required" : [ "Type" ]
    }
  },
  "properties" : {
    "CollectionEndpoint" : {
      "description" : "The endpoint for the collection.",
      "type" : "string"
    },
    "IndexName" : {
      "type" : "string",
      "pattern" : "^(?![_-])[a-z][a-z0-9_-]*$",
      "description" : "The name of the OpenSearch Serverless index."
    },
    "Settings" : {
      "$ref" : "#/definitions/IndexSettings",
      "description" : "Index settings"
    },
    "Mappings" : {
      "type" : "object",
      "description" : "Index Mappings",
      "additionalProperties" : False,
      "properties" : {
        "Properties" : {
          "type" : "object",
          "description" : "Defines the fields within the mapping, including their types and configurations",
          "additionalProperties" : False,
          "patternProperties" : {
            "^[A-Za-z0-9_.-]{1,64}$" : {
              "$ref" : "#/definitions/PropertyMapping",
              "description" : "Field name and its mapping configuration"
            }
          }
        }
      }
    },
    "Uuid" : {
      "description" : "The unique identifier for the index.",
      "type" : "string"
    }
  },
  "required" : [ "CollectionEndpoint", "IndexName" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/IndexName", "/properties/CollectionEndpoint" ],
  "readOnlyProperties" : [ "/properties/Uuid" ],
  "createOnlyProperties" : [ "/properties/IndexName", "/properties/CollectionEndpoint" ],
  "writeOnlyProperties" : [ "/properties/Settings/Index/RefreshInterval", "/properties/Settings/Index/KnnAlgoParamEfSearch" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "aoss:APIAccessAll" ]
    },
    "read" : {
      "permissions" : [ "aoss:APIAccessAll" ]
    },
    "update" : {
      "permissions" : [ "aoss:APIAccessAll" ]
    },
    "delete" : {
      "permissions" : [ "aoss:APIAccessAll" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "CollectionEndpoint" : {
            "$ref" : "resource-schema.json#/properties/CollectionEndpoint"
          }
        },
        "required" : [ "CollectionEndpoint" ]
      },
      "permissions" : [ "aoss:APIAccessAll" ]
    }
  }
}