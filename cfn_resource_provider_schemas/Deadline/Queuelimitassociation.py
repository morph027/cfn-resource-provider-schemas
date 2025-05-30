SCHEMA = {
  "typeName" : "AWS::Deadline::QueueLimitAssociation",
  "description" : "Definition of AWS::Deadline::QueueLimitAssociation Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-deadline",
  "properties" : {
    "FarmId" : {
      "type" : "string",
      "pattern" : "^farm-[0-9a-f]{32}$"
    },
    "LimitId" : {
      "type" : "string",
      "pattern" : "^limit-[0-9a-f]{32}$"
    },
    "QueueId" : {
      "type" : "string",
      "pattern" : "^queue-[0-9a-f]{32}$"
    }
  },
  "required" : [ "FarmId", "LimitId", "QueueId" ],
  "createOnlyProperties" : [ "/properties/FarmId", "/properties/LimitId", "/properties/QueueId" ],
  "primaryIdentifier" : [ "/properties/FarmId", "/properties/LimitId", "/properties/QueueId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "deadline:CreateQueueLimitAssociation", "deadline:GetQueueLimitAssociation", "identitystore:ListGroupMembershipsForMember" ]
    },
    "read" : {
      "permissions" : [ "deadline:GetQueueLimitAssociation", "identitystore:ListGroupMembershipsForMember" ]
    },
    "delete" : {
      "permissions" : [ "deadline:DeleteQueueLimitAssociation", "deadline:GetQueueLimitAssociation", "deadline:UpdateQueueLimitAssociation", "identitystore:ListGroupMembershipsForMember" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "FarmId" : {
            "$ref" : "resource-schema.json#/properties/FarmId"
          }
        },
        "required" : [ "FarmId" ]
      },
      "permissions" : [ "deadline:ListQueueLimitAssociations", "identitystore:ListGroupMembershipsForMember" ]
    }
  },
  "additionalProperties" : False
}