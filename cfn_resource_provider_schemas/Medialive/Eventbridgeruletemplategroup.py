SCHEMA = {
  "typeName" : "AWS::MediaLive::EventBridgeRuleTemplateGroup",
  "description" : "Definition of AWS::MediaLive::EventBridgeRuleTemplateGroup Resource Type",
  "definitions" : {
    "TagMap" : {
      "type" : "object",
      "description" : "Represents the tags associated with a resource.",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:.+:medialive:.+:eventbridge-rule-template-group:.+$",
      "description" : "An eventbridge rule template group's ARN (Amazon Resource Name)"
    },
    "CreatedAt" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 0,
      "description" : "A resource's optional description."
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 11,
      "minLength" : 7,
      "pattern" : "^(aws-)?[0-9]{7}$",
      "description" : "An eventbridge rule template group's id. AWS provided template groups have ids that start with `aws-`"
    },
    "Identifier" : {
      "type" : "string"
    },
    "ModifiedAt" : {
      "type" : "string",
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
  "required" : [ "Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/Id", "/properties/Identifier", "/properties/ModifiedAt" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/Identifier" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "medialive:CreateEventBridgeRuleTemplateGroup", "medialive:GetEventBridgeRuleTemplateGroup", "medialive:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "medialive:GetEventBridgeRuleTemplateGroup" ]
    },
    "update" : {
      "permissions" : [ "medialive:UpdateEventBridgeRuleTemplateGroup", "medialive:GetEventBridgeRuleTemplateGroup", "medialive:CreateTags", "medialive:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "medialive:DeleteEventBridgeRuleTemplateGroup" ]
    },
    "list" : {
      "permissions" : [ "medialive:ListEventBridgeRuleTemplateGroups" ]
    }
  },
  "additionalProperties" : False
}