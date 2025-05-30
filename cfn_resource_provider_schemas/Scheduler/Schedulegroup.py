SCHEMA = {
  "typeName" : "AWS::Scheduler::ScheduleGroup",
  "description" : "Definition of AWS::Scheduler::ScheduleGroup Resource Type",
  "definitions" : {
    "ScheduleGroupState" : {
      "type" : "string",
      "description" : "Specifies the state of the schedule group.",
      "enum" : [ "ACTIVE", "DELETING" ]
    },
    "Tag" : {
      "type" : "object",
      "description" : "Tag to associate with the resource.",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "Key for the tag"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "Value for the tag"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 1224,
      "minLength" : 1,
      "pattern" : "^arn:aws[a-z-]*:scheduler:[a-z0-9\\-]+:\\d{12}:schedule-group\\/[0-9a-zA-Z-_.]+$",
      "description" : "The Amazon Resource Name (ARN) of the schedule group."
    },
    "CreationDate" : {
      "type" : "string",
      "description" : "The time at which the schedule group was created.",
      "format" : "date-time"
    },
    "LastModificationDate" : {
      "type" : "string",
      "description" : "The time at which the schedule group was last modified.",
      "format" : "date-time"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 1,
      "pattern" : "^[0-9a-zA-Z-_.]+$"
    },
    "State" : {
      "$ref" : "#/definitions/ScheduleGroupState"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 0,
      "description" : "The list of tags to associate with the schedule group.",
      "insertionOrder" : False
    }
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreationDate", "/properties/LastModificationDate", "/properties/State" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "scheduler:TagResource", "scheduler:CreateScheduleGroup", "scheduler:GetScheduleGroup", "scheduler:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "scheduler:GetScheduleGroup", "scheduler:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "scheduler:TagResource", "scheduler:UntagResource", "scheduler:ListTagsForResource", "scheduler:GetScheduleGroup" ]
    },
    "delete" : {
      "permissions" : [ "scheduler:DeleteScheduleGroup", "scheduler:GetScheduleGroup", "scheduler:DeleteSchedule" ]
    },
    "list" : {
      "permissions" : [ "scheduler:ListScheduleGroups" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "scheduler:UntagResource", "scheduler:ListTagsForResource", "scheduler:TagResource" ]
  },
  "additionalProperties" : False
}