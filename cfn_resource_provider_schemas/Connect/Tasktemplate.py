SCHEMA = {
  "typeName" : "AWS::Connect::TaskTemplate",
  "description" : "Resource Type definition for AWS::Connect::TaskTemplate.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "Status" : {
      "description" : "The status of the task template",
      "type" : "string",
      "enum" : [ "ACTIVE", "INACTIVE" ]
    },
    "FieldType" : {
      "description" : "The type of the task template's field",
      "type" : "string",
      "enum" : [ "NAME", "DESCRIPTION", "SCHEDULED_TIME", "QUICK_CONNECT", "URL", "NUMBER", "TEXT", "TEXT_AREA", "DATE_TIME", "BOOLEAN", "SINGLE_SELECT", "EMAIL", "EXPIRY_DURATION", "SELF_ASSIGN" ]
    },
    "FieldIdentifier" : {
      "description" : "the identifier (name) for the task template field",
      "type" : "object",
      "properties" : {
        "Name" : {
          "description" : "The name of the task template field",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 100
        }
      },
      "additionalProperties" : False,
      "required" : [ "Name" ]
    },
    "FieldOption" : {
      "description" : "Single select field identifier",
      "type" : "string",
      "pattern" : "^[A-Za-z0-9](?:[A-Za-z0-9_.,\\s-]*[A-Za-z0-9_.,-])?$",
      "minLength" : 1,
      "maxLength" : 100
    },
    "Field" : {
      "description" : "A task template field object.",
      "type" : "object",
      "properties" : {
        "Id" : {
          "$ref" : "#/definitions/FieldIdentifier"
        },
        "Description" : {
          "description" : "The description of the task template's field",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 255
        },
        "Type" : {
          "$ref" : "#/definitions/FieldType"
        },
        "SingleSelectOptions" : {
          "description" : "list of field options to be used with single select",
          "type" : "array",
          "maxItems" : 50,
          "items" : {
            "$ref" : "#/definitions/FieldOption"
          }
        }
      },
      "additionalProperties" : False,
      "required" : [ "Id", "Type" ]
    },
    "InvisibleFieldInfo" : {
      "description" : "Invisible field info",
      "type" : "object",
      "properties" : {
        "Id" : {
          "$ref" : "#/definitions/FieldIdentifier"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Id" ]
    },
    "InvisibleTaskTemplateFields" : {
      "description" : "The list of the task template's invisible fields",
      "type" : "array",
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/InvisibleFieldInfo"
      }
    },
    "ReadOnlyFieldInfo" : {
      "description" : "ReadOnly field info",
      "type" : "object",
      "properties" : {
        "Id" : {
          "$ref" : "#/definitions/FieldIdentifier"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Id" ]
    },
    "ReadOnlyTaskTemplateFields" : {
      "description" : "The list of the task template's read only fields",
      "type" : "array",
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/ReadOnlyFieldInfo"
      }
    },
    "RequiredFieldInfo" : {
      "description" : "Required field info",
      "type" : "object",
      "properties" : {
        "Id" : {
          "$ref" : "#/definitions/FieldIdentifier"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Id" ]
    },
    "RequiredTaskTemplateFields" : {
      "description" : "The list of the task template's required fields",
      "type" : "array",
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/RequiredFieldInfo"
      }
    },
    "FieldValue" : {
      "description" : "the default value for the task template's field",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 4096
    },
    "DefaultFieldValue" : {
      "description" : "the default value for the task template's field",
      "type" : "object",
      "properties" : {
        "Id" : {
          "$ref" : "#/definitions/FieldIdentifier"
        },
        "DefaultValue" : {
          "$ref" : "#/definitions/FieldValue"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Id", "DefaultValue" ]
    },
    "ClientToken" : {
      "description" : "the client token string in uuid format",
      "type" : "string",
      "pattern" : "^$|[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$"
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. . You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "The identifier (arn) of the task template.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/task-template/[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12}$"
    },
    "InstanceArn" : {
      "description" : "The identifier (arn) of the instance.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$"
    },
    "Name" : {
      "description" : "The name of the task template.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100
    },
    "Description" : {
      "description" : "The description of the task template.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 255
    },
    "ContactFlowArn" : {
      "description" : "The identifier of the contact flow.",
      "type" : "string",
      "pattern" : "^$|arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/contact-flow/[-a-zA-Z0-9]*$"
    },
    "SelfAssignContactFlowArn" : {
      "description" : "The identifier of the contact flow.",
      "type" : "string",
      "pattern" : "^$|arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/contact-flow/[-a-zA-Z0-9]*$"
    },
    "Constraints" : {
      "description" : "The constraints for the task template",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InvisibleFields" : {
          "$ref" : "#/definitions/InvisibleTaskTemplateFields"
        },
        "RequiredFields" : {
          "$ref" : "#/definitions/RequiredTaskTemplateFields"
        },
        "ReadOnlyFields" : {
          "$ref" : "#/definitions/ReadOnlyTaskTemplateFields"
        }
      }
    },
    "Defaults" : {
      "description" : "",
      "type" : "array",
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/DefaultFieldValue"
      }
    },
    "Fields" : {
      "description" : "The list of task template's fields",
      "type" : "array",
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Field"
      }
    },
    "Status" : {
      "$ref" : "#/definitions/Status"
    },
    "ClientToken" : {
      "$ref" : "#/definitions/ClientToken"
    },
    "Tags" : {
      "description" : "One or more tags.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "InstanceArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:CreateTaskTemplate", "connect:TagResource" ]
    },
    "read" : {
      "permissions" : [ "connect:GetTaskTemplate" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "InstanceArn" : {
            "$ref" : "resource-schema.json#/properties/InstanceArn"
          }
        },
        "required" : [ "InstanceArn" ]
      },
      "permissions" : [ "connect:ListTaskTemplates" ]
    },
    "update" : {
      "permissions" : [ "connect:UpdateTaskTemplate", "connect:TagResource", "connect:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "connect:DeleteTaskTemplate", "connect:UntagResource", "connect:GetTaskTemplate" ]
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : False,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "connect:ListTagsForResource", "connect:UntagResource", "connect:TagResource" ]
  }
}