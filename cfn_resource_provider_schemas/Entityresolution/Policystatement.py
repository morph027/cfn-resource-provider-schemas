SCHEMA = {
  "typeName" : "AWS::EntityResolution::PolicyStatement",
  "description" : "Policy Statement defined in AWS Entity Resolution Service",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-entity-resolution.git",
  "definitions" : {
    "VeniceGlobalArn" : {
      "description" : "Arn of the resource to which the policy statement is being attached.",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:((schemamapping|matchingworkflow|idmappingworkflow|idnamespace)/[a-zA-Z_0-9-]{1,255})$"
    },
    "StatementId" : {
      "description" : "The Statement Id of the policy statement that is being attached.",
      "type" : "string",
      "pattern" : "^[0-9A-Za-z]+$",
      "minLength" : 1,
      "maxLength" : 64
    },
    "StatementEffect" : {
      "type" : "string",
      "enum" : [ "Allow", "Deny" ]
    },
    "StatementAction" : {
      "type" : "string",
      "pattern" : "^(entityresolution:[a-zA-Z0-9]+)$",
      "minLength" : 3,
      "maxLength" : 64
    },
    "StatementActionList" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/StatementAction"
      }
    },
    "StatementPrincipal" : {
      "type" : "string",
      "pattern" : "^(\\\\d{12})|([a-z0-9\\\\.]+)$",
      "minLength" : 12,
      "maxLength" : 64
    },
    "StatementPrincipalList" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/StatementPrincipal"
      }
    },
    "StatementCondition" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 40960
    }
  },
  "properties" : {
    "Arn" : {
      "$ref" : "#/definitions/VeniceGlobalArn"
    },
    "StatementId" : {
      "$ref" : "#/definitions/StatementId"
    },
    "Effect" : {
      "$ref" : "#/definitions/StatementEffect"
    },
    "Action" : {
      "$ref" : "#/definitions/StatementActionList"
    },
    "Principal" : {
      "$ref" : "#/definitions/StatementPrincipalList"
    },
    "Condition" : {
      "$ref" : "#/definitions/StatementCondition"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "Arn", "StatementId" ],
  "createOnlyProperties" : [ "/properties/StatementId", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn", "/properties/StatementId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "entityresolution:AddPolicyStatement" ]
    },
    "read" : {
      "permissions" : [ "entityresolution:GetPolicy" ]
    },
    "update" : {
      "permissions" : [ "entityresolution:AddPolicyStatement", "entityresolution:DeletePolicyStatement" ]
    },
    "delete" : {
      "permissions" : [ "entityresolution:DeletePolicyStatement", "entityresolution:GetPolicy" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "Arn" : {
            "$ref" : "resource-schema.json#/properties/Arn"
          }
        },
        "required" : [ "Arn" ]
      },
      "permissions" : [ "entityresolution:GetPolicy" ]
    }
  }
}