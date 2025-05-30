SCHEMA = {
  "typeName" : "AWS::Lightsail::Disk",
  "description" : "Resource Type definition for AWS::Lightsail::Disk",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lightsail.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ],
      "additionalProperties" : False
    },
    "AutoSnapshotAddOn" : {
      "description" : "An object that represents additional parameters when enabling or modifying the automatic snapshot add-on",
      "type" : "object",
      "properties" : {
        "SnapshotTimeOfDay" : {
          "type" : "string",
          "description" : "The daily time when an automatic snapshot will be created.",
          "pattern" : "^[0-9]{2}:00$"
        }
      },
      "additionalProperties" : False
    },
    "AddOn" : {
      "description" : "A addon associate with a resource.",
      "type" : "object",
      "properties" : {
        "AddOnType" : {
          "type" : "string",
          "description" : "The add-on type",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Status" : {
          "type" : "string",
          "description" : "Status of the Addon",
          "enum" : [ "Enabling", "Disabling", "Enabled", "Terminating", "Terminated", "Disabled", "Failed" ]
        },
        "AutoSnapshotAddOnRequest" : {
          "$ref" : "#/definitions/AutoSnapshotAddOn"
        }
      },
      "required" : [ "AddOnType" ],
      "additionalProperties" : False
    },
    "Location" : {
      "description" : "Location of a resource.",
      "type" : "object",
      "properties" : {
        "AvailabilityZone" : {
          "type" : "string",
          "description" : "The Availability Zone in which to create your disk. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request."
        },
        "RegionName" : {
          "type" : "string",
          "description" : "The Region Name in which to create your disk."
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DiskName" : {
      "description" : "The names to use for your new Lightsail disk.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9][\\w\\-.]*[a-zA-Z0-9]$",
      "minLength" : 1,
      "maxLength" : 254
    },
    "DiskArn" : {
      "type" : "string"
    },
    "SupportCode" : {
      "description" : "Support code to help identify any issues",
      "type" : "string"
    },
    "AvailabilityZone" : {
      "description" : "The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Location" : {
      "$ref" : "#/definitions/Location"
    },
    "ResourceType" : {
      "description" : "Resource type of Lightsail instance.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "AddOns" : {
      "description" : "An array of objects representing the add-ons to enable for the new instance.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/AddOn"
      }
    },
    "State" : {
      "description" : "State of the Lightsail disk",
      "type" : "string"
    },
    "AttachmentState" : {
      "description" : "Attachment State of the Lightsail disk",
      "type" : "string"
    },
    "SizeInGb" : {
      "description" : "Size of the Lightsail disk",
      "type" : "integer"
    },
    "Iops" : {
      "description" : "Iops of the Lightsail disk",
      "type" : "integer"
    },
    "IsAttached" : {
      "description" : "Check is Disk is attached state",
      "type" : "boolean"
    },
    "Path" : {
      "description" : "Path of the  attached Disk",
      "type" : "string"
    },
    "AttachedTo" : {
      "description" : "Name of the attached Lightsail Instance",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "DiskName", "SizeInGb" ],
  "readOnlyProperties" : [ "/properties/AttachedTo", "/properties/Path", "/properties/IsAttached", "/properties/Iops", "/properties/AttachmentState", "/properties/State", "/properties/ResourceType", "/properties/Location/AvailabilityZone", "/properties/Location/RegionName", "/properties/SupportCode", "/properties/DiskArn" ],
  "primaryIdentifier" : [ "/properties/DiskName" ],
  "createOnlyProperties" : [ "/properties/DiskName", "/properties/AvailabilityZone", "/properties/SizeInGb" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lightsail:CreateDisk", "lightsail:EnableAddOn", "lightsail:DisableAddOn", "lightsail:GetDisk", "lightsail:GetDisks", "lightsail:GetRegions", "lightsail:TagResource", "lightsail:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "lightsail:GetDisk", "lightsail:GetDisks" ]
    },
    "delete" : {
      "permissions" : [ "lightsail:GetDisk", "lightsail:GetDisks", "lightsail:DeleteDisk" ]
    },
    "list" : {
      "permissions" : [ "lightsail:GetDisks" ]
    },
    "update" : {
      "permissions" : [ "lightsail:GetDisk", "lightsail:GetDisks", "lightsail:EnableAddOn", "lightsail:DisableAddOn", "lightsail:TagResource", "lightsail:UntagResource" ],
      "timeoutInMinutes" : 2160
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "lightsail:TagResource", "lightsail:UntagResource" ]
  }
}