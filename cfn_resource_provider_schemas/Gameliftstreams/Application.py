SCHEMA = {
  "typeName" : "AWS::GameLiftStreams::Application",
  "description" : "Definition of AWS::GameLiftStreams::Application Resource Type",
  "definitions" : {
    "RuntimeEnvironment" : {
      "type" : "object",
      "properties" : {
        "Version" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        },
        "Type" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "required" : [ "Type", "Version" ],
      "additionalProperties" : False
    },
    "Tags" : {
      "type" : "object",
      "maxProperties" : 50,
      "minProperties" : 1,
      "patternProperties" : {
        ".+" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
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
    "ApplicationLogOutputUri" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 0,
      "pattern" : "^$|^s3://([a-zA-Z0-9][a-zA-Z0-9._-]{1,61}[a-zA-Z0-9])(/[a-zA-Z0-9._-]+)*/?$"
    },
    "ApplicationLogPaths" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 1024,
        "minLength" : 0
      },
      "maxItems" : 10,
      "minItems" : 0,
      "insertionOrder" : False
    },
    "ApplicationSourceUri" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 1
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 128,
      "minLength" : 1,
      "pattern" : "^(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^:\n]*):([0-9]{12}):([^:\n]*)$)$"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 80,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*$"
    },
    "ExecutablePath" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 1
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 32,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-]+$"
    },
    "RuntimeEnvironment" : {
      "$ref" : "#/definitions/RuntimeEnvironment"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "required" : [ "ApplicationSourceUri", "Description", "ExecutablePath", "RuntimeEnvironment" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/ApplicationSourceUri", "/properties/RuntimeEnvironment", "/properties/ExecutablePath" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "gameliftstreams:CreateApplication", "gameliftstreams:GetApplication", "gameliftstreams:TagResource", "gameliftstreams:ListTagsForResource", "s3:GetObject", "s3:ListBucket" ]
    },
    "read" : {
      "permissions" : [ "gameliftstreams:GetApplication", "gameliftstreams:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "gameliftstreams:UpdateApplication", "gameliftstreams:GetApplication", "gameliftstreams:TagResource", "gameliftstreams:UntagResource", "gameliftstreams:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "gameliftstreams:DeleteApplication", "gameliftstreams:GetApplication" ]
    },
    "list" : {
      "permissions" : [ "gameliftstreams:ListApplications", "gameliftstreams:ListTagsForResource" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "gameliftstreams:TagResource", "gameliftstreams:UntagResource", "gameliftstreams:ListTagsForResource" ]
  },
  "additionalIdentifiers" : [ [ "/properties/Id" ] ]
}