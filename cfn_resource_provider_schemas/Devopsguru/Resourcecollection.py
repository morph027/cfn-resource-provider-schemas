SCHEMA = {
  "typeName" : "AWS::DevOpsGuru::ResourceCollection",
  "description" : "This resource schema represents the ResourceCollection resource in the Amazon DevOps Guru.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-devops-guru",
  "definitions" : {
    "ResourceCollectionFilter" : {
      "description" : "Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.",
      "type" : "object",
      "properties" : {
        "CloudFormation" : {
          "$ref" : "#/definitions/CloudFormationCollectionFilter"
        },
        "Tags" : {
          "$ref" : "#/definitions/TagCollections"
        }
      },
      "additionalProperties" : False
    },
    "CloudFormationCollectionFilter" : {
      "description" : "CloudFormation resource for DevOps Guru to monitor",
      "type" : "object",
      "properties" : {
        "StackNames" : {
          "description" : "An array of CloudFormation stack names.",
          "type" : "array",
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 128,
            "pattern" : "^[a-zA-Z*]+[a-zA-Z0-9-]*$"
          },
          "minItems" : 1,
          "maxItems" : 1000,
          "insertionOrder" : False
        }
      },
      "additionalProperties" : False
    },
    "TagCollections" : {
      "description" : "Tagged resources for DevOps Guru to monitor",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/TagCollection"
      },
      "insertionOrder" : False
    },
    "TagCollection" : {
      "description" : "Tagged resource for DevOps Guru to monitor",
      "type" : "object",
      "properties" : {
        "AppBoundaryKey" : {
          "description" : "A Tag key for DevOps Guru app boundary.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "TagValues" : {
          "description" : "Tag values of DevOps Guru app boundary.",
          "type" : "array",
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 256
          },
          "minItems" : 1,
          "maxItems" : 1000,
          "insertionOrder" : False
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ResourceCollectionFilter" : {
      "$ref" : "#/definitions/ResourceCollectionFilter"
    },
    "ResourceCollectionType" : {
      "description" : "The type of ResourceCollection",
      "type" : "string",
      "enum" : [ "AWS_CLOUD_FORMATION", "AWS_TAGS" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "ResourceCollectionFilter" ],
  "readOnlyProperties" : [ "/properties/ResourceCollectionType" ],
  "primaryIdentifier" : [ "/properties/ResourceCollectionType" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "devops-guru:UpdateResourceCollection", "devops-guru:GetResourceCollection" ]
    },
    "read" : {
      "permissions" : [ "devops-guru:GetResourceCollection" ]
    },
    "delete" : {
      "permissions" : [ "devops-guru:UpdateResourceCollection", "devops-guru:GetResourceCollection" ]
    },
    "list" : {
      "permissions" : [ "devops-guru:GetResourceCollection" ]
    },
    "update" : {
      "permissions" : [ "devops-guru:UpdateResourceCollection", "devops-guru:GetResourceCollection" ]
    }
  }
}