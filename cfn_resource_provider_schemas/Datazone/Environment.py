SCHEMA = {
  "typeName" : "AWS::DataZone::Environment",
  "description" : "Definition of AWS::DataZone::Environment Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datazone",
  "definitions" : {
    "EnvironmentParameter" : {
      "type" : "object",
      "description" : "The parameter details of an environment.",
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "The name of an environment parameter."
        },
        "Value" : {
          "type" : "string",
          "description" : "The value of an environment parameter."
        }
      },
      "additionalProperties" : False
    },
    "EnvironmentStatus" : {
      "type" : "string",
      "description" : "The status of the Amazon DataZone environment.",
      "enum" : [ "ACTIVE", "CREATING", "UPDATING", "DELETING", "CREATE_FAILED", "UPDATE_FAILED", "DELETE_FAILED", "VALIDATION_FAILED", "SUSPENDED", "DISABLED", "EXPIRED", "DELETED", "INACCESSIBLE" ]
    }
  },
  "properties" : {
    "AwsAccountId" : {
      "type" : "string",
      "description" : "The AWS account in which the Amazon DataZone environment is created.",
      "pattern" : "^\\d{12}$"
    },
    "AwsAccountRegion" : {
      "type" : "string",
      "description" : "The AWS region in which the Amazon DataZone environment is created.",
      "pattern" : "^[a-z]{2}-[a-z]{4,10}-\\d$"
    },
    "EnvironmentAccountIdentifier" : {
      "type" : "string",
      "description" : "The AWS account in which the Amazon DataZone environment is created.",
      "pattern" : "^\\d{12}$"
    },
    "EnvironmentAccountRegion" : {
      "type" : "string",
      "description" : "The AWS region in which the Amazon DataZone environment is created.",
      "pattern" : "^[a-z]{2}-[a-z]{4,10}-\\d$"
    },
    "CreatedAt" : {
      "type" : "string",
      "description" : "The timestamp of when the environment was created.",
      "format" : "date-time"
    },
    "CreatedBy" : {
      "type" : "string",
      "description" : "The Amazon DataZone user who created the environment."
    },
    "Description" : {
      "type" : "string",
      "description" : "The description of the Amazon DataZone environment.",
      "maxLength" : 2048
    },
    "DomainId" : {
      "type" : "string",
      "description" : "The identifier of the Amazon DataZone domain in which the environment is created.",
      "pattern" : "^dzd[-_][a-zA-Z0-9_-]{1,36}$"
    },
    "DomainIdentifier" : {
      "type" : "string",
      "description" : "The identifier of the Amazon DataZone domain in which the environment would be created.",
      "pattern" : "^dzd[-_][a-zA-Z0-9_-]{1,36}$"
    },
    "EnvironmentBlueprintId" : {
      "type" : "string",
      "description" : "The ID of the blueprint with which the Amazon DataZone environment was created.",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
    },
    "EnvironmentProfileId" : {
      "type" : "string",
      "description" : "The ID of the environment profile with which the Amazon DataZone environment was created.",
      "pattern" : "^[a-zA-Z0-9_-]{0,36}$"
    },
    "EnvironmentProfileIdentifier" : {
      "type" : "string",
      "description" : "The ID of the environment profile with which the Amazon DataZone environment would be created.",
      "pattern" : "^[a-zA-Z0-9_-]{0,36}$"
    },
    "GlossaryTerms" : {
      "type" : "array",
      "insertionOrder" : False,
      "description" : "The glossary terms that can be used in the Amazon DataZone environment.",
      "items" : {
        "type" : "string",
        "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
      },
      "maxItems" : 20,
      "minItems" : 1
    },
    "EnvironmentRoleArn" : {
      "type" : "string",
      "description" : "Environment role arn for custom aws environment permissions"
    },
    "Id" : {
      "type" : "string",
      "description" : "The ID of the Amazon DataZone environment.",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the environment.",
      "maxLength" : 64,
      "minLength" : 1,
      "pattern" : "^[\\w -]+$"
    },
    "ProjectId" : {
      "type" : "string",
      "description" : "The ID of the Amazon DataZone project in which the environment is created.",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
    },
    "ProjectIdentifier" : {
      "type" : "string",
      "description" : "The ID of the Amazon DataZone project in which the environment would be created.",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$"
    },
    "Provider" : {
      "type" : "string",
      "description" : "The provider of the Amazon DataZone environment."
    },
    "Status" : {
      "$ref" : "#/definitions/EnvironmentStatus",
      "description" : "The status of the Amazon DataZone environment."
    },
    "UpdatedAt" : {
      "type" : "string",
      "description" : "The timestamp of when the environment was updated.",
      "format" : "date-time"
    },
    "UserParameters" : {
      "type" : "array",
      "insertionOrder" : False,
      "description" : "The user parameters of the Amazon DataZone environment.",
      "items" : {
        "$ref" : "#/definitions/EnvironmentParameter"
      }
    }
  },
  "required" : [ "Name", "ProjectIdentifier", "DomainIdentifier" ],
  "readOnlyProperties" : [ "/properties/AwsAccountId", "/properties/AwsAccountRegion", "/properties/CreatedAt", "/properties/CreatedBy", "/properties/DomainId", "/properties/EnvironmentBlueprintId", "/properties/EnvironmentProfileId", "/properties/Id", "/properties/ProjectId", "/properties/Provider", "/properties/Status", "/properties/UpdatedAt" ],
  "writeOnlyProperties" : [ "/properties/EnvironmentProfileIdentifier", "/properties/ProjectIdentifier", "/properties/DomainIdentifier", "/properties/EnvironmentAccountIdentifier", "/properties/EnvironmentAccountRegion", "/properties/EnvironmentRoleArn" ],
  "createOnlyProperties" : [ "/properties/DomainIdentifier", "/properties/EnvironmentProfileIdentifier", "/properties/ProjectIdentifier", "/properties/UserParameters", "/properties/EnvironmentAccountIdentifier", "/properties/EnvironmentAccountRegion" ],
  "primaryIdentifier" : [ "/properties/DomainId", "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/DomainIdentifier" ] ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "datazone:CreateEnvironment", "datazone:GetEnvironment", "datazone:DeleteEnvironment", "datazone:AssociateEnvironmentRole", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "datazone:GetEnvironment" ]
    },
    "update" : {
      "permissions" : [ "datazone:UpdateEnvironment", "datazone:GetEnvironment", "datazone:DeleteEnvironment", "datazone:AssociateEnvironmentRole", "datazone:DisassociateEnvironmentRole", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "datazone:DeleteEnvironment", "datazone:GetEnvironment" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DomainIdentifier" : {
            "$ref" : "resource-schema.json#/properties/DomainIdentifier"
          },
          "ProjectIdentifier" : {
            "$ref" : "resource-schema.json#/properties/ProjectIdentifier"
          }
        },
        "required" : [ "DomainIdentifier", "ProjectIdentifier" ]
      },
      "permissions" : [ "datazone:ListEnvironments" ]
    }
  },
  "additionalProperties" : False
}