<?php

/**
 * This file contains a migration script for creating the `tbl_orders` table in Laravel.
 */

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    /**
     * Run the migration to create the `tbl_orders` table.
     */
    public function up(): void
    {
        // Create the `tbl_orders` table
        Schema::create('tbl_orders', function (Blueprint $table) {
            // Add an auto-incrementing primary key column named `id`
            $table->id();

            // Add two timestamps columns named `created_at` and `updated_at`
            $table->timestamps();

            // Allow NULL values for the `name` column
            $table->string('name')->nullable();

            // Allow NULL values for the `description` column
            $table->text('description')->nullable();

            // Set the default value of `pending` for the `status` column
            $table->string('status')->default('pending');
        });
    }

    /**
     * Revert the migration by dropping the `tbl_orders` table.
     */
    public function down(): void
    {
        // Drop the `tbl_orders` table if it exists
        Schema::dropIfExists('tbl_orders');
    }
};
