<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
  /**
   * Run the migrations.
   */
  public function up(): void
  {
    Schema::create('tbl_orders', function (Blueprint $table) {
      $table->id();
      $table->timestamps();

      // allow null values for name column
      $table->string('name')->nullable(); 
      
      $table->text('description')->nullable(); // allow null values for description column

      $table->string('status')->default('pending'); // set default value 'pending' for status column
    });
  }

  /**
   * Reverse the migrations.
   */
  public function down(): void
  {
    Schema::dropIfExists('tbl_orders');
  }
};
//
