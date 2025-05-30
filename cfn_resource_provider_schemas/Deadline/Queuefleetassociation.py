SCHEMA = {
  "typeName" : "AWS::Deadline::QueueFleetAssociation",
  "description" : "Definition of AWS::Deadline::QueueFleetAssociation Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-deadline",
  "properties" : {
    "FarmId" : {
      "type" : "string",
      "pattern" : "^farm-[0-9a-f]{32}$"
    },
    "FleetId" : {
      "type" : "string",
      "pattern" : "^fleet-[0-9a-f]{32}$"
    },
    "QueueId" : {
      "type" : "string",
      "pattern" : "^queue-[0-9a-f]{32}$"
    }
  },
  "required" : [ "FarmId", "FleetId", "QueueId" ],
  "createOnlyProperties" : [ "/properties/FarmId", "/properties/FleetId", "/properties/QueueId" ],
  "primaryIdentifier" : [ "/properties/FarmId", "/properties/FleetId", "/properties/QueueId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "deadline:CreateQueueFleetAssociation", "deadline:GetQueueFleetAssociation", "identitystore:ListGroupMembershipsForMember" ]
    },
    "read" : {
      "permissions" : [ "deadline:GetQueueFleetAssociation", "identitystore:ListGroupMembershipsForMember" ]
    },
    "delete" : {
      "permissions" : [ "deadline:DeleteQueueFleetAssociation", "deadline:GetQueueFleetAssociation", "deadline:UpdateQueueFleetAssociation", "identitystore:ListGroupMembershipsForMember" ]
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
      "permissions" : [ "deadline:ListQueueFleetAssociations", "identitystore:ListGroupMembershipsForMember" ]
    }
  },
  "additionalProperties" : False
}