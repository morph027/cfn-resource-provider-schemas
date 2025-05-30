SCHEMA = {
  "typeName" : "AWS::Deadline::QueueEnvironment",
  "description" : "Definition of AWS::Deadline::QueueEnvironment Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-deadline",
  "definitions" : {
    "EnvironmentTemplateType" : {
      "type" : "string",
      "enum" : [ "JSON", "YAML" ]
    }
  },
  "properties" : {
    "FarmId" : {
      "type" : "string",
      "pattern" : "^farm-[0-9a-f]{32}$"
    },
    "Name" : {
      "type" : "string"
    },
    "Priority" : {
      "type" : "integer",
      "maximum" : 10000,
      "minimum" : 0
    },
    "QueueEnvironmentId" : {
      "type" : "string",
      "pattern" : "^queueenv-[0-9a-f]{32}$"
    },
    "QueueId" : {
      "type" : "string",
      "pattern" : "^queue-[0-9a-f]{32}$"
    },
    "Template" : {
      "type" : "string",
      "maxLength" : 15000,
      "minLength" : 1
    },
    "TemplateType" : {
      "$ref" : "#/definitions/EnvironmentTemplateType"
    }
  },
  "required" : [ "FarmId", "QueueId", "Priority", "Template", "TemplateType" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "createOnlyProperties" : [ "/properties/FarmId", "/properties/QueueId" ],
  "readOnlyProperties" : [ "/properties/Name", "/properties/QueueEnvironmentId" ],
  "primaryIdentifier" : [ "/properties/FarmId", "/properties/QueueId", "/properties/QueueEnvironmentId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "deadline:CreateQueueEnvironment", "identitystore:ListGroupMembershipsForMember" ]
    },
    "read" : {
      "permissions" : [ "deadline:GetQueueEnvironment", "identitystore:ListGroupMembershipsForMember" ]
    },
    "update" : {
      "permissions" : [ "deadline:UpdateQueueEnvironment", "identitystore:ListGroupMembershipsForMember" ]
    },
    "delete" : {
      "permissions" : [ "deadline:DeleteQueueEnvironment", "deadline:GetQueueEnvironment", "identitystore:ListGroupMembershipsForMember" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "FarmId" : {
            "$ref" : "resource-schema.json#/properties/FarmId"
          },
          "QueueId" : {
            "$ref" : "resource-schema.json#/properties/QueueId"
          }
        },
        "required" : [ "FarmId", "QueueId" ]
      },
      "permissions" : [ "deadline:ListQueueEnvironments", "identitystore:ListGroupMembershipsForMember" ]
    }
  },
  "additionalProperties" : False
}