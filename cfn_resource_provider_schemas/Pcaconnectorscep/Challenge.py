SCHEMA = {
  "typeName" : "AWS::PCAConnectorSCEP::Challenge",
  "description" : "Represents a SCEP Challenge that is used for certificate enrollment",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-pcaconnectorscep",
  "definitions" : {
    "Tags" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "Unit" : {
      "type" : "object",
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ChallengeArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\\d*:\\d{12}:connector\\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\\/challenge\\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$"
    },
    "ConnectorArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\\d*:\\d{12}:connector\\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "pca-connector-scep:ListTagsForResource", "pca-connector-scep:TagResource", "pca-connector-scep:UntagResource" ]
  },
  "required" : [ "ConnectorArn" ],
  "readOnlyProperties" : [ "/properties/ChallengeArn" ],
  "createOnlyProperties" : [ "/properties/ConnectorArn" ],
  "primaryIdentifier" : [ "/properties/ChallengeArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "pca-connector-scep:CreateChallenge", "pca-connector-scep:TagResource" ]
    },
    "read" : {
      "permissions" : [ "pca-connector-scep:ListTagsForResource", "pca-connector-scep:GetChallengeMetadata" ]
    },
    "delete" : {
      "permissions" : [ "pca-connector-scep:GetChallengeMetadata", "pca-connector-scep:DeleteChallenge", "pca-connector-scep:UntagResource" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ConnectorArn" : {
            "$ref" : "resource-schema.json#/properties/ConnectorArn"
          }
        },
        "required" : [ "ConnectorArn" ]
      },
      "permissions" : [ "pca-connector-scep:ListChallengeMetadata" ]
    },
    "update" : {
      "permissions" : [ "pca-connector-scep:ListTagsForResource", "pca-connector-scep:TagResource", "pca-connector-scep:UntagResource" ]
    }
  },
  "additionalProperties" : False
}