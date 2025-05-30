SCHEMA = {
  "typeName" : "AWS::DataZone::EnvironmentActions",
  "description" : "Definition of AWS::DataZone::EnvironmentActions Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datazone",
  "definitions" : {
    "EnvironmentActionURI" : {
      "type" : "string",
      "description" : "The URI of the console link specified as part of the environment action.",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "AwsConsoleLinkParameters" : {
      "type" : "object",
      "description" : "The parameters of the console link specified as part of the environment action",
      "properties" : {
        "Uri" : {
          "$ref" : "#/definitions/EnvironmentActionURI"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Description" : {
      "type" : "string",
      "description" : "The description of the Amazon DataZone environment action.",
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
    "EnvironmentId" : {
      "type" : "string",
      "description" : "The identifier of the Amazon DataZone environment in which the action is taking place",
      "pattern" : "[a-zA-Z0-9_-]{1,36}$",
      "maxLength" : 36,
      "minLength" : 1
    },
    "EnvironmentIdentifier" : {
      "type" : "string",
      "description" : "The identifier of the Amazon DataZone environment in which the action is taking place",
      "pattern" : "[a-zA-Z0-9_-]{1,36}$",
      "maxLength" : 36,
      "minLength" : 1
    },
    "Id" : {
      "type" : "string",
      "description" : "The ID of the Amazon DataZone environment action.",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$",
      "maxLength" : 36,
      "minLength" : 1
    },
    "Identifier" : {
      "type" : "string",
      "description" : "The ID of the Amazon DataZone environment action.",
      "pattern" : "^[a-zA-Z0-9_-]{1,36}$",
      "maxLength" : 36,
      "minLength" : 1
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the environment action.",
      "maxLength" : 64,
      "minLength" : 1,
      "pattern" : "^[\\w -]+$"
    },
    "Parameters" : {
      "description" : "The parameters of the environment action.",
      "$ref" : "#/definitions/AwsConsoleLinkParameters"
    }
  },
  "required" : [ "Name" ],
  "readOnlyProperties" : [ "/properties/DomainId", "/properties/EnvironmentId", "/properties/Id" ],
  "writeOnlyProperties" : [ "/properties/EnvironmentIdentifier", "/properties/DomainIdentifier", "/properties/Identifier" ],
  "createOnlyProperties" : [ "/properties/DomainIdentifier", "/properties/EnvironmentIdentifier" ],
  "primaryIdentifier" : [ "/properties/DomainId", "/properties/EnvironmentId", "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/EnvironmentIdentifier" ] ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "datazone:CreateEnvironmentAction", "datazone:GetEnvironmentAction", "datazone:DeleteEnvironmentAction" ]
    },
    "read" : {
      "permissions" : [ "datazone:GetEnvironmentAction" ]
    },
    "update" : {
      "permissions" : [ "datazone:UpdateEnvironmentAction", "datazone:GetEnvironmentAction", "datazone:DeleteEnvironmentAction" ]
    },
    "delete" : {
      "permissions" : [ "datazone:DeleteEnvironmentAction", "datazone:GetEnvironmentAction" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DomainIdentifier" : {
            "$ref" : "resource-schema.json#/properties/DomainIdentifier"
          },
          "EnvironmentIdentifier" : {
            "$ref" : "resource-schema.json#/properties/EnvironmentIdentifier"
          }
        },
        "required" : [ "DomainIdentifier", "EnvironmentIdentifier" ]
      },
      "permissions" : [ "datazone:ListEnvironmentActions" ]
    }
  },
  "additionalProperties" : False
}