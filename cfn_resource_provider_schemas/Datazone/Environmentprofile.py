SCHEMA = {
  "typeName" : "AWS::DataZone::EnvironmentProfile",
  "description" : "AWS Datazone Environment Profile is pre-configured set of resources and blueprints that provide reusable templates for creating environments.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datazone",
  "definitions" : {
    "EnvironmentParameter" : {
      "type" : "object",
      "description" : "The parameter details of an environment profile.",
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "The name of an environment profile parameter."
        },
        "Value" : {
          "type" : "string",
          "description" : "The value of an environment profile parameter."
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "AwsAccountId" : {
      "description" : "The AWS account in which the Amazon DataZone environment is created.",
      "type" : "string",
      "pattern" : "^\\d{12}$"
    },
    "AwsAccountRegion" : {
      "description" : "The AWS region in which this environment profile is created.",
      "type" : "string",
      "pattern" : "^[a-z]{2}-[a-z]{4,10}-\\d$"
    },
    "CreatedAt" : {
      "description" : "The timestamp of when this environment profile was created.",
      "type" : "string",
      "format" : "date-time"
    },
    "CreatedBy" : {
      "description" : "The Amazon DataZone user who created this environment profile.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of this Amazon DataZone environment profile.",
      "type" : "string",
      "maxLength" : 2048
    },
    "DomainId" : {
      "description" : "The ID of the Amazon DataZone domain in which this environment profile is created.",
      "type" : "string",
      "pattern" : "^dzd[-_][a-zA-Z0-9_-]{1,36}$"
    },
    "DomainIdentifier" : {
      "description" : "The ID of the Amazon DataZone domain in which this environment profile is created.",
      "type" : "string",
      "pattern" : "^dzd[-_][a-zA-Z0-9_-]{1,36}$"
    },
    "EnvironmentBlueprintId" : {
      "description" : "The ID of the blueprint with which this environment profile is created.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
    },
    "EnvironmentBlueprintIdentifier" : {
      "description" : "The ID of the blueprint with which this environment profile is created.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
    },
    "Id" : {
      "description" : "The ID of this Amazon DataZone environment profile.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
    },
    "Name" : {
      "description" : "The name of this Amazon DataZone environment profile.",
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 1,
      "pattern" : "^[\\w -]+$"
    },
    "ProjectId" : {
      "description" : "The identifier of the project in which to create the environment profile.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
    },
    "ProjectIdentifier" : {
      "description" : "The identifier of the project in which to create the environment profile.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
    },
    "UpdatedAt" : {
      "description" : "The timestamp of when this environment profile was updated.",
      "type" : "string",
      "format" : "date-time"
    },
    "UserParameters" : {
      "description" : "The user parameters of this Amazon DataZone environment profile.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/EnvironmentParameter"
      }
    }
  },
  "required" : [ "EnvironmentBlueprintIdentifier", "ProjectIdentifier", "DomainIdentifier", "AwsAccountId", "AwsAccountRegion", "Name" ],
  "readOnlyProperties" : [ "/properties/CreatedAt", "/properties/CreatedBy", "/properties/DomainId", "/properties/EnvironmentBlueprintId", "/properties/Id", "/properties/ProjectId", "/properties/UpdatedAt" ],
  "writeOnlyProperties" : [ "/properties/EnvironmentBlueprintIdentifier", "/properties/ProjectIdentifier", "/properties/DomainIdentifier" ],
  "createOnlyProperties" : [ "/properties/DomainIdentifier", "/properties/EnvironmentBlueprintIdentifier", "/properties/ProjectIdentifier" ],
  "primaryIdentifier" : [ "/properties/DomainId", "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/DomainIdentifier" ] ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "datazone:CreateEnvironmentProfile", "datazone:GetEnvironmentProfile" ]
    },
    "read" : {
      "permissions" : [ "datazone:GetEnvironmentProfile" ]
    },
    "update" : {
      "permissions" : [ "datazone:UpdateEnvironmentProfile", "datazone:GetEnvironmentProfile" ]
    },
    "delete" : {
      "permissions" : [ "datazone:DeleteEnvironmentProfile", "datazone:GetEnvironmentProfile" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DomainIdentifier" : {
            "$ref" : "resource-schema.json#/properties/DomainIdentifier"
          }
        },
        "required" : [ "DomainIdentifier" ]
      },
      "permissions" : [ "datazone:ListEnvironmentProfiles" ]
    }
  },
  "additionalProperties" : False
}