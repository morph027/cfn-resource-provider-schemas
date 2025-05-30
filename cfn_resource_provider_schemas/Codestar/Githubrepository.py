SCHEMA = {
  "typeName" : "AWS::CodeStar::GitHubRepository",
  "description" : "Resource Type definition for AWS::CodeStar::GitHubRepository",
  "additionalProperties" : False,
  "properties" : {
    "EnableIssues" : {
      "type" : "boolean"
    },
    "ConnectionArn" : {
      "type" : "string"
    },
    "RepositoryName" : {
      "type" : "string"
    },
    "RepositoryAccessToken" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "RepositoryOwner" : {
      "type" : "string"
    },
    "IsPrivate" : {
      "type" : "boolean"
    },
    "Code" : {
      "$ref" : "#/definitions/Code"
    },
    "RepositoryDescription" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "S3" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ObjectVersion" : {
          "type" : "string"
        },
        "Bucket" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Bucket", "Key" ]
    },
    "Code" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3" : {
          "$ref" : "#/definitions/S3"
        }
      },
      "required" : [ "S3" ]
    }
  },
  "required" : [ "RepositoryName", "RepositoryOwner" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}