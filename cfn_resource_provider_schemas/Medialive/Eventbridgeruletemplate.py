SCHEMA = {
  "typeName" : "AWS::MediaLive::EventBridgeRuleTemplate",
  "description" : "Definition of AWS::MediaLive::EventBridgeRuleTemplate Resource Type",
  "definitions" : {
    "EventBridgeRuleTemplateEventType" : {
      "type" : "string",
      "description" : "The type of event to match with the rule.",
      "enum" : [ "MEDIALIVE_MULTIPLEX_ALERT", "MEDIALIVE_MULTIPLEX_STATE_CHANGE", "MEDIALIVE_CHANNEL_ALERT", "MEDIALIVE_CHANNEL_INPUT_CHANGE", "MEDIALIVE_CHANNEL_STATE_CHANGE", "MEDIAPACKAGE_INPUT_NOTIFICATION", "MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION", "MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION", "SIGNAL_MAP_ACTIVE_ALARM", "MEDIACONNECT_ALERT", "MEDIACONNECT_SOURCE_HEALTH", "MEDIACONNECT_OUTPUT_HEALTH", "MEDIACONNECT_FLOW_STATUS_CHANGE" ]
    },
    "EventBridgeRuleTemplateTarget" : {
      "type" : "object",
      "description" : "The target to which to send matching events.",
      "properties" : {
        "Arn" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1,
          "pattern" : "^arn.+$",
          "description" : "Target ARNs must be either an SNS topic or CloudWatch log group."
        }
      },
      "required" : [ "Arn" ],
      "additionalProperties" : False
    },
    "TagMap" : {
      "type" : "object",
      "description" : "Represents the tags associated with a resource.",
      "patternProperties" : {
        ".+" : {
          "type" : "string",
          "description" : "Placeholder documentation for __string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:.+:medialive:.+:eventbridge-rule-template:.+$",
      "description" : "An eventbridge rule template's ARN (Amazon Resource Name)"
    },
    "CreatedAt" : {
      "type" : "string",
      "description" : "Placeholder documentation for __timestampIso8601",
      "format" : "date-time"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 0,
      "description" : "A resource's optional description."
    },
    "EventTargets" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/EventBridgeRuleTemplateTarget"
      },
      "description" : "Placeholder documentation for __listOfEventBridgeRuleTemplateTarget"
    },
    "EventType" : {
      "$ref" : "#/definitions/EventBridgeRuleTemplateEventType"
    },
    "GroupId" : {
      "type" : "string",
      "maxLength" : 11,
      "minLength" : 7,
      "pattern" : "^(aws-)?[0-9]{7}$",
      "description" : "An eventbridge rule template group's id. AWS provided template groups have ids that start with `aws-`"
    },
    "GroupIdentifier" : {
      "type" : "string",
      "pattern" : "^[^\\s]+$",
      "description" : "An eventbridge rule template group's identifier. Can be either be its id or current name."
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 11,
      "minLength" : 7,
      "pattern" : "^(aws-)?[0-9]{7}$",
      "description" : "An eventbridge rule template's id. AWS provided templates have ids that start with `aws-`"
    },
    "Identifier" : {
      "type" : "string",
      "description" : "Placeholder documentation for __string"
    },
    "ModifiedAt" : {
      "type" : "string",
      "description" : "Placeholder documentation for __timestampIso8601",
      "format" : "date-time"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^[^\\s]+$",
      "description" : "A resource's name. Names must be unique within the scope of a resource type in a specific region."
    },
    "Tags" : {
      "$ref" : "#/definitions/TagMap"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "medialive:CreateTags", "medialive:DeleteTags" ]
  },
  "required" : [ "EventType", "Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/GroupId", "/properties/Id", "/properties/Identifier", "/properties/ModifiedAt" ],
  "writeOnlyProperties" : [ "/properties/GroupIdentifier" ],
  "createOnlyProperties" : [ "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/Identifier" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "medialive:CreateEventBridgeRuleTemplate", "medialive:GetEventBridgeRuleTemplate", "medialive:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "medialive:GetEventBridgeRuleTemplate" ]
    },
    "update" : {
      "permissions" : [ "medialive:UpdateEventBridgeRuleTemplate", "medialive:GetEventBridgeRuleTemplate", "medialive:CreateTags", "medialive:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "medialive:DeleteEventBridgeRuleTemplate" ]
    },
    "list" : {
      "permissions" : [ "medialive:ListEventBridgeRuleTemplates" ]
    }
  },
  "additionalProperties" : False
}